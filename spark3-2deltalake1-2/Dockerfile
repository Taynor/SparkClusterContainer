#Pull latest Ubuntu image
FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

#Configure the path directories for spark, python and java
RUN export SPARK_HOME=/usr/local/bin/spark-3.2.1-bin-hadoop3.2
RUN export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
RUN export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH
RUN export JAVA_HOME=/usr/lib/jvm/open-jdk

#Install python3 and pip3 and java runtime 11
RUN apt upgrade
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y openjdk-8-jre 
RUN apt install -y openjdk-8-jdk
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install pyspark
RUN pip3 install delta-spark

#Copy the files to the working directory for the image
COPY . .

#Make the delta-lake-install.sh an executable
RUN chmod +x delta-lake-install.sh

#Start the spark cluster
CMD /bin/bash /usr/local/bin/spark-3.2.1-bin-hadoop3.2/sbin/start-master.sh && /usr/local/bin/spark-3.2.1-bin-hadoop3.2/bin/spark-shell && /usr/local/bin/delta-lake-install.sh