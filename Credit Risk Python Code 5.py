import mysql.connector

connection = mysql.connector.connect(

host='localhost',

user='root',

password='D_18032005_s',

database='credit_risk_db'

)

print(

"SQL Connection Successful"

)
