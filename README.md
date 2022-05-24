# Spark Cluster Container
Local Spark cluster container images and example scripts. Can be used for interactive and automated use, including delta lake and non delta lake samples. Docker is used to create the images, which is built from the latest Ubuntu base image.

The solution has been updated with the Spark version 3.2.1 and the delta lake 1.2.0 (As from 24/05/2022)

This repo is using Spark version 3.1.2, delta lake project 1.0.0, python 3.8, pip3 and open Java SDK and runtime 8. 

The container comes packaged with the numpy, pandas and pyspark supporting modules as part of the Docker image. For the spark download go to https://spark.apache.org/downloads.html for the delta lake download go to https://docs.delta.io/1.0.0/quick-start.html. Ensure the dowloaded packages are unzipped before moving them to their respective folders.

Non delta lake spark cluster

![image](https://user-images.githubusercontent.com/59668937/134163802-c166b92d-7394-431f-a822-0f3e20e563e4.png)

Delta lake spark cluster

![image](https://user-images.githubusercontent.com/59668937/134163868-ccc520d1-3654-4305-9238-21446ee66268.png)


For ease it uses the available /usr/local/bin path in the VM container, as the working directory. 

Use the following command to start up the container (this snippet used PowerShell to run docker):

docker run --tty --volume ${PWD}:/usr/local/bin -p <portNumber:portNumber> -d <image name>
  
To run any of the example scripts point to the respective python scripts:
  
python3 /usr/local/bin/<script_name.py>
  
python3 /usr/local/bin/testdf.py -- use for basic dataframe example
  
python3 /usr/local/bin/delta-lake-test.py -- use for creating delta lake table from a basic dataframe
  
python3 /usr/local/bin/delta-lake-test-csv.py -- use for creating delta lake table from a dummy csv file included in the sample
