# Task 6

Deleting all images except of chosen one
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
