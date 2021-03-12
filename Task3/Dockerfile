# How to expose port
# https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/

FROM httpd
MAINTAINER pm2021 <239676@edu.p.lodz.pl>
LABEL org.label-schema.description="Przykładowa strona WWW"
COPY ./public-html /usr/local/apache2/htdocs/
EXPOSE 80

# Run this command in order to show the result
# docker build -t "httpd_exposed" .
# docker run -dit -P httpd_exposed -> Flag P set random port
# docker ps -> copy the port fg.  0.0.0.0:32773->80/tcp
# paste to browser localhost:32773 -> change port for this shown in docker ps
