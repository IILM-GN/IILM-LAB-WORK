""" WAP in python to take 5 datasets from the user : Name , Gender , Age , Performance , Height 
    and then show them as a table with rows and columns and hence we have tell that the all the main categories (ROWS) are what type of attributes : 
    Ordinal , Nominal , Binary , Numeric (if numeric then what is it's sub category either discrete or continuos)"""

#03/08/2026 
#Monday
#DVA LAB 


num = int(input("How many people's data do you want to enter? "))

names = []
genders = []
ages = []
performances = []
heights = []

for i in range(num):
    print("\n--- Person", i + 1, "---")
    name = input("Enter Name          : ")
    gender = input("Enter Gender        : ")
    age = int(input("Enter Age           : "))
    performance = input("Enter Performance\n(Low/Medium/High)  : ")
    height = float(input("Enter Height (in cm): "))

    names.append(name)
    genders.append(gender)
    ages.append(age)
    performances.append(performance)
    heights.append(height)


print("\n")
print("=" * 70)
print("                       DATA TABLE")
print("=" * 70)


header = f"{'Name':<15}{'Gender':<15}{'Age':<10}{'Performance':<15}{'Height(cm)':<12}"
print(header)
print("-" * 70)

for i in range(num):
    row = f"{names[i]:<15}{genders[i]:<15}{ages[i]:<10}{performances[i]:<15}{heights[i]:<12}"
    print(row)
    print("-" * 70)

print("\n")
print("=" * 55)
print("                  ATTRIBUTE CLASSIFICATION")
print("=" * 55)
print(f"{'Attribute':<16}{'Type':<12}{'Sub-Type'}")
print("-" * 55)
print(f"{'Name':<16}{'Nominal':<12}{'-'}")
print("-" * 55)
print(f"{'Gender':<16}{'Nominal':<12}{'-'}")
print("-" * 55)
print(f"{'Age':<16}{'Numeric':<12}{'Discrete'}")
print("-" * 55)
print(f"{'Performance':<16}{'Ordinal':<12}{'-'}")
print("-" * 55)
print(f"{'Height':<16}{'Numeric':<12}{'Continuous'}")
print("=" * 55)


print("\n")
print("=" * 65)
print("           MEANING OF ATTRIBUTE TYPES")
print("=" * 65)
print()
print("Nominal Attribute:")
print("  These contain names or labels WITHOUT any natural ordering.")
print("  Examples: Name, Gender, Color, City")
print()
print("Ordinal Attribute:")
print("  These have a MEANINGFUL ORDER or ranking, but the gaps between")
print("  values are not equal or measurable.")
print("  Examples: Performance (Low < Medium < High), Education Level, Grade")
print()
print("Binary Attribute:")
print("  A special case of nominal with ONLY TWO possible categories/values.")
print("  Examples: Yes/No, True/False, Male/Female")
print()
print("Numeric Attribute - Discrete:")
print("  These are numerical values that can only take SPECIFIC COUNTABLE")
print("  values (usually whole numbers). They result from COUNTING.")
print("  Examples: Age (in years), Number of children, Count of items")
print()
print("Numeric Attribute - Continuous:")
print("  These are numerical values that can take ANY VALUE within a range.")
print("  They can include decimals/fractions and result from MEASURING.")
print("  Examples: Height, Weight, Temperature, Time")
print()
print("=" * 65)
