import pandas as pd

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Credit Risk.csv")

print(df.head())

print("\nDataset Shape")

print(df.shape)

print("\nAverage Income")

print(df['Income'].mean())

print("\nAverage Credit Score")

print(df['Credit_Score'].mean())

print("\nHighest Loan Amount")

print(df['Loan_Amount'].max())
