FROM mysql:5.7
ENV MYSQL_DATABASE='orders'
ENV MYSQL_ROOT_PASSWORD='password'
ADD orders.sql /docker-entrypoint-initdb.d
