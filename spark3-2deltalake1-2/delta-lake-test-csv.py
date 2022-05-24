#Import delta lake and pyspark modules functions
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

#This is the configuration for spark to use delta lake at a local node level
builder = SparkSession.builder.appName("MyApp").master("local[*]").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension").config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

#Create a df from reading a csv
sparkDF = spark.read.csv("usr/local/bin/csvexample.csv", header="true", inferSchema="true")        

#Create the dummy delta lake table
sparkDF.write.format("delta").save("/usr/local/bin")

#Read the dummy data lake table
dfData = spark.read.format("delta").load("/usr/local/bin")
dfData.show()