#Import delta lake and pyspark modules functions
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

#This is the configuration for spark to use delta lake at a local node level
builder = SparkSession.builder.appName("MyApp").master("local[*]").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension").config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

#Data set to convert into a df
data = [(1, "tmcnally", "taynor.mcnally@email.com", "Taynor", "McNally", "IT", "DevOps", "Engineer", "Matthew Murdoch"), 
(2, "jjones", "jessica.jones@email.com", "Jessica", "Jones", "IT", "DevOps", "Engineer", "Matthew Murdoch"),
(3, "drand", "danny.rand@email.com", "Danny", "Rand", "IT", "DevOps", "Engineer", "Matthew Murdoch"),
(4, "mmurdoch", "matt.murdoch@email.com", "Matthew", "Murdoch", "IT", "DevOps", "Manager", "Tony Stark")]

#Create df
column_row = ['UserID','UserName', 'Email', 'FirstName', 'LastName', 'Department', 'TeamName', 'Role', 'Manager']
df = spark.createDataFrame(data, column_row)

#Convert to RDD
sc = spark.sparkContext
rdddf = sc.parallelize(data)
newdf = spark.createDataFrame(rdddf)

#Create the dummy delta lake table
newdf.write.format("delta").save("/usr/local/bin")

#Read the dummy data lake table
df = spark.read.format("delta").load("/usr/local/bin")
df.show()