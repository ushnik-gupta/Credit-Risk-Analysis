import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='D_18032005_s',
    database='credit_risk_db'
)

query = "SELECT * FROM credit_data"

cursor = connection.cursor()
cursor.execute(query)

rows = cursor.fetchall()

columns = [i[0] for i in cursor.description]

df = pd.DataFrame(rows, columns=columns)

print(df)

print("\nTotal Records:", len(df))

cursor.close()
connection.close()
