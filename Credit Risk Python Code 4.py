import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Credit Risk.csv")

plt.figure(figsize=(8,5))

sns.histplot(

df['Credit_Score'],

bins=10

)

plt.title(

'Credit Score Distribution'

)

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(

x='Risk_Level',

data=df

)

plt.title(

'Risk Level Distribution'

)

plt.show()
