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

```

## With docker-compose

### Basic command
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
```

```


### Frontend
```

```
