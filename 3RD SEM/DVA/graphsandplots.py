#26th October 2026
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("plot.csv")

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Charts from plot.csv", fontsize=16)

monthly_sales = df.groupby("month", sort=False)["sales"].sum()
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker="o", color="royalblue")
axes[0, 0].set(title="Monthly Sales", xlabel="Month", ylabel="Sales")
axes[0, 0].grid(True, alpha=0.3)

category_sales = df.groupby("category")["sales"].sum()
axes[0, 1].bar(category_sales.index, category_sales.values, color="seagreen")
axes[0, 1].set(title="Sales by Category", xlabel="Category", ylabel="Sales")

axes[0, 2].hist(df["test_score"], bins=10, color="darkorange", edgecolor="black")
axes[0, 2].set(title="Distribution of Test Scores", xlabel="Test Score", ylabel="Count")

axes[1, 0].pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Share of Sales by Category")

axes[1, 1].scatter(df["study_hours"], df["test_score"], color="purple", alpha=0.7)
axes[1, 1].set(title="Study Hours vs. Test Scores", xlabel="Study Hours", ylabel="Test Score")
axes[1, 1].grid(True, alpha=0.3)

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
