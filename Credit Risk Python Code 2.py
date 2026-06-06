import pandas as pd

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Credit Risk.csv")

print(df.head())

print("\nDataset Shape")

print(df.shape)

print("\nMissing Values")

print(df.isnull().sum())

print("\nAverage Income")

print(df['Income'].mean())

print("\nAverage Credit Score")

print(df['Credit_Score'].mean())

print("\nHighest Loan Amount")

print(df['Loan_Amount'].max())

print("\nRisk Level Analysis")

print(

df.groupby(

'Risk_Level'

)[

['Income',

'Credit_Score']

]

.mean()

)

print("\nLoan Status Analysis")

print(

df.groupby(

'Loan_Status'

)['Loan_Amount']

.mean()

)

print("\nCorrelation Matrix")

print(

df[

['Age',

'Income',

'Loan_Amount',

'Credit_Score',

'Employment_Years']

]

.corr()

)

