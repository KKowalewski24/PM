# Task 6

Deleting all images except of chosen one
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "2fb283157d3c" | grep -v "f18da2f58c3d")
```

## Message Broker - RabbitMQ


## Centralized Logging - ELK (Logstash + Elasticsearch + Kibana)
[Image used in this sub task](https://elk-docker.readthedocs.io/)
[Tutorial used for this sub task](https://soshace.com/visualizing-logs-from-a-dockerized-node-application-using-the-elastic-stack/)

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

Filebeats have been installed locally on Windows - instruction is in above tutorial
* Download the Filebeat Windows zip file from the downloads page.
* Extract the contents of the zip file into C:\Program Files.
* Rename the filebeat-<version>-windows directory to Filebeat.
* Open a PowerShell prompt as an Administrator (right-click the PowerShell icon and select Run As Administrator).
* From the PowerShell prompt, run the following commands to install Filebeat as a Windows service:
```
cd 'C:\Program Files\Filebeat'
.\install-service-filebeat.ps1
```

Filebeat.yml setup
```
filebeat.inputs:

# Each - is an input. Most options can be set at the input level, so
# you can use different inputs for various configurations.
# Below are the input specific configurations.

- type: docker
  containers.ids: "*"

  # Change to true to enable this input configuration.
  enabled: true

output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["localhost:9200"]
  index: "filebeat-%{[agent.version]}-%{+yyyy.MM.dd}"
```
Open Powershell with admin privileges
```
cd 'C:\Program Files\Filebeat'
.\filebeat.exe setup --dashboards
Start-Service filebeat
```
http://localhost:5601/app/infra#/logs/stream

## Microservices Replication - JMeter

