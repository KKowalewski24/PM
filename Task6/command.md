# Task 6

Deleting all images except of chosen one
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "2fb283157d3c" | grep -v "f18da2f58c3d")
```

## Message Broker - RabbitMQ


## Centralized Logging - ELK (Logstash + Elasticsearch + Kibana)
[Image used in this sub task](https://elk-docker.readthedocs.io/)

Remember to setup `vm.max_map_count`
On Windows do the following steps
```
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```
On Linux run in your host machine
* `vim /etc/sysctl.conf`
* Add `vm.max_map_count=262144`
* restart
```
## Microservices Replication - JMeter

