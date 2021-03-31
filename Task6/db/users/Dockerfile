FROM mysql:5.7
ENV MYSQL_DATABASE='users'
MYSQL_ROOT_PASSWORD='password'
ADD users.sql /docker-entrypoint-initdb.d
