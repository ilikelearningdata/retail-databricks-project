# Retail ETL Project Using Databricks and PySpark

## Project Overview
This project demonstrates a simple ETL pipeline using **Azure/AWS Databricks and PySpark**. It processes retail order data, filters valid records, and calculates total sales and order counts by city.

## Technologies Used
- Databricks
- PySpark
- Python
- GitHub
- Delta Lake (optional)

## Project Structure
```text
retail-databricks-project/
├── README.md
└── retail_etl.py
```

## Data Description
The project uses sample retail order data with the following columns:

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer | Customer name |
| city | Customer's city |
| amount | Order amount |

## ETL Workflow
1. **Extract:** Create a Spark DataFrame from sample retail data.
2. **Transform:** Filter orders where the amount is greater than zero.
3. **Aggregate:** Calculate total sales and order counts by city.
4. **Load (optional):** Save the aggregated results in Delta format.
5. **Version control:** Store the source code in GitHub and track changes.

## Expected Output
| City | Total Sales | Total Orders |
|---|---:|---:|
| Chennai | 800 | 2 |
| Bangalore | 1900 | 2 |
| Hyderabad | 900 | 1 |

## How to Run
1. Clone or connect the GitHub repository to your Databricks workspace.
2. Open `retail_etl.py` in a Databricks notebook or configure it as a Python/S
