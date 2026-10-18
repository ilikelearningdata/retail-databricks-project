
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

# Create Spark session
spark = SparkSession.builder.appName("RetailETL").getOrCreate()

# Sample retail data
data = [
    (101, "Alice", "Chennai", 500),
    (102, "Bob", "Bangalore", 700),
    (103, "Charlie", "Chennai", 300),
    (104, "David", "Hyderabad", 900),
    (105, "Eva", "Bangalore", 1200),
]

columns = ["order_id", "customer", "city", "amount"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

print("Source Data:")
df.show()

# Transform: keep valid orders
clean_df = df.filter(col("amount") > 0)

# Aggregate sales by city
result_df = clean_df.groupBy("city").agg(
    sum("amount").alias("total_sales"),
    count("order_id").alias("total_orders")
)

print("Sales by City:")
result_df.show()

# Optional: save results as Delta
# Change this path to a location you can write to.
# result_df.write.format("delta").mode("overwrite").save(
#     "/tmp/retail_sales_by_city"
# )
