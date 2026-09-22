"""
07/09/2026
Exp 3 : Load, clean, and preprocess a real-world dataset using Pandas 
(handling missing values, duplicates, outliers, and data transformation).
"""
import pandas as pd
import numpy as np

pd.set_option("display.float_format", "{:.2f}".format)
pd.set_option("display.max_columns", None)

df = pd.read_csv(
    r"X:\IILM-LAB\3RD SEM\DVA\students.csv",
    dtype={"Admission_No": str, "Phone_Number": str},
    na_values=["", "NA", "NaN", "nan", "Null", "null", "N/A", "-", "?"]
)

print("Initial shape:", df.shape)
print("Missing values:\n", df.isna().sum())

df = df.dropna(subset=["Admission_No", "Name"])

df["Admission_No"] = (
    df["Admission_No"].str.strip().str.upper()
    .str.replace("AMD", "ADM", regex=False)
)

df["Name"] = (
    df["Name"].str.strip()
    .str.replace(r"[^A-Za-z '\-]", "", regex=True)
    .str.strip()
)
df = df[df["Name"].str.len() > 1]

df["Class"] = df["Class"].astype(str).str.strip().str.lower().str.replace(".", "", regex=False)
class_map = {
    "1st year": "1st Year", "first year": "1st Year", "1 year": "1st Year", "1st yr": "1st Year", "1 yr": "1st Year",
    "2nd year": "2nd Year", "2nd yr": "2nd Year", "second year": "2nd Year", "2nd": "2nd Year",
    "3rd year": "3rd Year", "third year": "3rd Year", "3rd yr": "3rd Year"
}
df = df[df["Class"].isin(class_map.keys())].copy()
df["Class"] = df["Class"].map(class_map)

df["Branch"] = df["Branch"].astype(str).str.strip().str.upper().str.replace(".", "", regex=False).str.replace(" ", "", regex=False)
branch_map = {
    "CSE": "CSE", "CS": "CSE", "COMPUTERSCIENCE": "CSE", "COMPUTERSCI": "CSE",
    "ECE": "ECE", "E&CE": "ECE",
    "IT": "IT",
    "EEE": "EEE", "EE": "EEE",
    "MECH": "MECH", "MECHANICAL": "MECH",
    "CIVIL": "CIVIL"
}
df = df[df["Branch"].isin(branch_map.keys())].copy()
df["Branch"] = df["Branch"].map(branch_map)

df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace(r"\D", "", regex=True).str[-10:]
df.loc[df["Phone_Number"].str.len() != 10, "Phone_Number"] = np.nan

df["CGPA"] = pd.to_numeric(df["CGPA"], errors="coerce")

before = len(df)
df = df.drop_duplicates(subset="Admission_No", keep="first").reset_index(drop=True)
print(f"Removed {before - len(df)} rows (by Admission No) -> {len(df)} rows")

before = len(df)
df = df.drop_duplicates(subset=["Name", "Class", "Branch", "Phone_Number"], keep="first").reset_index(drop=True)
print(f"Removed {before - len(df)} rows (identity) -> {len(df)} rows")

df["Name"] = df["Name"].str.title()

rng = np.random.default_rng(42)
missing_phone = df["Phone_Number"].isna()
generated = ["9" + "".join(rng.choice(10, 9).astype(str)) for _ in range(int(missing_phone.sum()))]
df.loc[missing_phone, "Phone_Number"] = generated
print(f"Regenerated {int(missing_phone.sum())} invalid/missing phone numbers")

print(f"Missing CGPA before imputation: {df['CGPA'].isna().sum()}")
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].median()).round(2)

out_of_range = df[(df["CGPA"] < 0) | (df["CGPA"] > 10)]
print(f"Out-of-range CGPAs to clip: {len(out_of_range)}")

df["CGPA"] = df["CGPA"].clip(lower=0, upper=10).round(2)

df["Class"] = pd.Categorical(df["Class"], categories=["1st Year", "2nd Year", "3rd Year"], ordered=True)

df["CGPA_Category"] = pd.cut(
    df["CGPA"],
    bins=[0, 6, 8, 10],
    labels=["Poor", "Average", "Excellent"],
    include_lowest=True
)

df = pd.get_dummies(df, columns=["Branch"], prefix="", prefix_sep="", dtype=int)

df = df.rename(columns={
    "Admission_No": "Admission Number",
    "Name": "Name",
    "Class": "Class",
    "Phone_Number": "Phone Number",
    "CGPA": "CGPA"
})

df = df[["Admission Number", "Name", "Class", "Phone Number", "CGPA", "CGPA_Category"] +
        [c for c in df.columns if c in ["CSE", "ECE", "IT", "EEE", "MECH", "CIVIL"]]]

df.to_csv(r"X:\IILM-LAB\3RD SEM\DVA\students_clean.csv", index=False)

print("\nFinal shape:", df.shape)
print("Remaining missing:", df.isna().sum().sum())
print("\nColumns:", list(df.columns))
print("\nCGPA stats:\n", df["CGPA"].describe())
print("\nStudents per class:\n", df["Class"].value_counts())
print("\nStudents per branch:\n", df[[c for c in df.columns if c in ["CSE", "ECE", "IT", "EEE", "MECH", "CIVIL"]]].sum())
print("\nCGPA categories:\n", df["CGPA_Category"].value_counts())
print("\nPreview:\n", df.head(10))