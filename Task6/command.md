# Task 6

Deleting all images except of chosen one
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "2fb283157d3c" | grep -v "f18da2f58c3d")
```

## Message Broker - RabbitMQ


## Centralized Logging - ELK (Logstash + Elasticsearch + Kibana)


## Microservices Replication - JMeter

