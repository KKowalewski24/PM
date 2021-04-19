# Task 6

Deleting all images except of chosen images - work in bash - on Windows use git bash
```
docker image rm -f $(docker images | grep -v "1b5eb721624e" | grep -v "cd0f0b1e283d" | grep -v "f18da2f58c3d" | grep -v "72ab4137bd85")
```

## Message Broker - RabbitMQ
Go to `Task6-RabbitMQ` directory and run `docker-compose up` in order to start.

This sub task has been created in Flask(Python) - The project from `Task6` directory
has not been used

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

Somehow on my PC after running whole docker-compose it does not work - in order to show how it works leave only elk and email_service

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
