import pandas as pd

df = pd.read_csv(
    r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Credit Risk.csv"
)

df.to_excel(
    r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Credit_Risk.xlsx",
    index=False
)

print("Excel Export Successful")
