# Task 6

Deleting all images except of chosen one
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "2fb283157d3c" | grep -v "f18da2f58c3d")
```

## Message Broker - RabbitMQ
Go to `Task6-RabbitMQ` directory and run `docker-compose up` in order to start.

This sub task has been created in Flask(Python) - The project from `Task6` directory
has not been used

## Centralized Logging - ELK (Logstash + Elasticsearch + Kibana)


## Microservices Replication - JMeter

