# Task 5

## Without docker-compose

### MySQL Database
```
docker build -t sample_mysql .
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password sample_mysql
docker exec -it CONTAINER_ID bash
mysql -uroot -p
show databases;
use products;
show tables;
select * from products;
```

### Backend
```
docker build -t sample_backend .
docker run -it -p 8081:8081 sample_backend
```

### Frontend
```
docker build -t sample_frontend .
docker run -it -p 8080:8080 sample_frontend
```

## With docker-compose

### Basic commands
```
// create and start containers
docker-compose up
// start services with detached mode
docker-compose -d up
// start specific service
docker-compose up <service-name>
// list images
docker-compose images
// list containers
docker-compose ps
// start service
docker-compose start
// stop services
docker-compose stop
// display running containers
docker-compose top
// kill services
docker-compose kill
// remove stopped containers
docker-compose rm
// stop all contaners and remove images, volumes
docker-compose down
```
### Create and start containers
```
docker-compose up
```

### MySQL Database
```
docker exec -it CONTAINER_ID bash
mysql -uroot -p
show databases;
use products;
show tables;
select * from products;
```

### Backend
Everything is done by docker-compose


### Frontend
Everything is done by docker-compose
