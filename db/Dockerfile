#Database container
FROM mysql:8.4

MAINTAINER MYSQL
LABEL RUN="docker run -it --name ifotosdb --ipc=host --net=host --pid=host -v /data:/data -d ifotosdb:2.0"

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
#ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
#ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD


#RUN microdnf install -y git
RUN chown -R mysql:mysql /var/lib/mysql/
RUN mkdir /data
RUN chown -R mysql:mysql /data
COPY my.cnf /etc/my.cnf

#RUN git clone https://github.com/ifriedman7/IFotos.git
#WORKDIR IFotos
#RUN /usr/bin/pip3 install -r requirements.txt

# Set default command
#CMD ["/usr/bin/bash"]
EXPOSE 3306
# Start the MySQL server when the container is run
CMD ["mysqld"]
#RUN systemctl start mysqld
