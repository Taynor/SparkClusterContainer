# Spark Cluster Container
Local Spark cluster container images and example scripts. Can be used for interactive and automated use, including delta lake and non delta lake samples. Docker is used to create the images, which is built from the latest Ubuntu base image.

This repo is using Spark version 3.1.2, python 3.8, pip3 and open Java SDK and runtime 8. 

The container comes packaged with the numpy, pandas and pyspark supporting modules.

For ease it uses the available /usr/local/bin path in the VM container, as the working directory. The wokring directory includes a copy of the spark runtime, for each sample. The delta lake sample uses version 1.0.0, which is included in the packaged folder.

Use the following command to start up the container (this snippet used PowerShell to run docker):

docker run --tty --volume ${PWD}:/usr/local/bin -p <portNumber:portNumber> -d <image name>
  
To run any of the example scripts point to the respective python scripts:
  
python3 /usr/local/bin/<script_name.py>
  
python3 /usr/local/bin/testdf.py -- use for basic dataframe example
  
python3 /usr/local/bin/delta-lake-test.py -- use for creating delta lake table from a basic dataframe
  
python3 /usr/local/bin/delta-lake-test-csv.py -- use for creating delta lake table from a dummy csv file included in the sample
