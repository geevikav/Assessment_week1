import pandas as pd

df = pd.read_csv("data/employee.csv")

print("Employee Data:")
print(df)

print("\nTotal Employees:")
print(len(df))

print("\nAverage Salary:")
print(df["salary"].mean())

print("\nDepartment-wise Average Salary:")
print(df.groupby("department")["salary"].mean())

print("\nEmployees from Chennai:")
print(df[df["city"] == "Chennai"])

print("\nCity-wise Employee Count:")
print(df["city"].value_counts())