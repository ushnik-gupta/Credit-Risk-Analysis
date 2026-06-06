CREATE DATABASE credit_risk_db;

USE credit_risk_db;

CREATE TABLE credit_data (
Customer_ID VARCHAR(20),
Age INT,
Income FLOAT,
Loan_Amount FLOAT,
Credit_Score INT,
Employment_Years INT,
Loan_Status VARCHAR(30),
Risk_Level VARCHAR(30)
);

INSERT INTO credit_data
VALUES
('C001',25,45000,150000,710,3,'Approved','Low'),
('C002',41,90000,350000,820,10,'Approved','Low'),
('C003',35,32000,200000,560,2,'Rejected','High'),
('C004',28,55000,180000,690,4,'Approved','Medium'),
('C005',52,120000,450000,790,15,'Approved','Low'),
('C006',31,28000,250000,510,1,'Rejected','High'),
('C007',44,65000,300000,670,8,'Approved','Medium'),
('C008',29,38000,220000,590,2,'Rejected','High');

SELECT * FROM credit_data;

SELECT
AVG(Income)
AS Average_Income
FROM credit_data;

SELECT
AVG(Credit_Score)
AS Average_Credit_Score
FROM credit_data;

SELECT
MAX(Loan_Amount)
AS Highest_Loan
FROM credit_data;

SELECT
Risk_Level,
AVG(Income)
AS Average_Income,
AVG(Credit_Score)
AS Average_Credit_Score
FROM credit_data
GROUP BY Risk_Level;

SELECT
Loan_Status,
COUNT(*) AS Total_Customers,
AVG(Loan_Amount) AS Average_Loan
FROM credit_data
GROUP BY Loan_Status;

SELECT
Customer_ID,
Credit_Score,
CASE
WHEN Credit_Score>=750
THEN 'LOW RISK'
WHEN Credit_Score BETWEEN 650 AND 749
THEN 'MEDIUM RISK'
ELSE 'HIGH RISK'
END AS Risk_Category
FROM credit_data;

SELECT
Risk_Level,
AVG(Loan_Amount)
AS Avg_Loan
FROM credit_data
GROUP BY Risk_Level
HAVING AVG(Loan_Amount)>200000;

SELECT
Customer_ID,
Credit_Score,
RANK() OVER(
ORDER BY Credit_Score DESC
)
AS Credit_Rank
FROM credit_data;

SELECT
COUNT(*) AS Total_Customers,
AVG(Income) AS Avg_Income,
AVG(Credit_Score) AS Avg_Credit_Score,
MAX(Loan_Amount) AS Highest_Loan_Amount
FROM credit_data;