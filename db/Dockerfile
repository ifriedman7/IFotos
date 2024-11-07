#Database container
FROM mysql:8.4

LABEL RUN="docker run -it --name ifotosdb --ipc=host --net=host --pid=host -v /data:/data -d ifotosdb:2.0"

RUN chown -R mysql:mysql /var/lib/mysql/
RUN mkdir /data
RUN chown -R mysql:mysql /data
COPY my.cnf /etc/my.cnf

# Set default command
#CMD ["/usr/bin/bash"]
EXPOSE 3306
# Start the MySQL server when the container is run
CMD ["mysqld"]
#RUN systemctl start mysqld

