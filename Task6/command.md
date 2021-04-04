# Task 6

Deleting all images except of chosen images
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "cd0f0b1e283d" | grep -v "f18da2f58c3d" | grep -v "72ab4137bd85")
```

## Message Broker - RabbitMQ


## Centralized Logging - ELK (Logstash + Elasticsearch + Kibana)


## Microservices Replication - JMeter

```
docker-compose up --scale product_service=5
```

[How to install and run JMeter](https://www.guru99.com/guide-to-install-jmeter.html)

* Install JDK 1.8
* Copy all dirs and files from zip archive
* Go to bin and run jmeter.bat - this starts JMeter GUI
* Right click on `Test Plan` then click `open` and then choose `GetProducts.jmx` file
* In order to run test go to `GetProductsTable` and click green traingle at top bar - in table you will see the result - in order to stop click stop button - in case of many threads you have to wait a little bit to stop - take a look at console with running docker-compose
* In `Thread Group` you can set number of threads and in `GetProductsTable` you can see all details in time of executing test
