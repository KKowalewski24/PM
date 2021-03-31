FROM mysql:5.7
ENV MYSQL_DATABASE='products'
ENV MYSQL_ROOT_PASSWORD='password'
ADD products.sql /docker-entrypoint-initdb.d
