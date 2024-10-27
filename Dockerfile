FROM quay.io/centos/centos:stream9
#MAINTAINER The CentOS Project <cloud-ops@centos.org
#Database container
ENV container docker
LABEL RUN="docker run -it --name ifotosdb --ipc=host --net=host --pid=host -e HOST=/host -e NAME=NAME -e IMAGE=IMAGE -v /sys/fs/selinux:/sys/fs/selinux:ro -v /data:/data -v /run:/run -v /var/log:/var/log -v /etc/localtime:/etc/localtime -v /:/host IMAGE"

#RUN rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
RUN rpm -Uvh https://dev.mysql.com/get/mysql84-community-release-el9-1.noarch.rpm
RUN sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/mysql-community.repo
RUN yum -y --enablerepo=mysql-community install \ 
           mysql-community-server \
           mysql-devel \
           mysql \
           mysql-common \
           mysql-libs \
           mysql-community-devel

#RUN git clone https://github.com/ifriedman7/IFotos.git
WORKDIR IFotos
#RUN /usr/bin/pip3 install -r requirements.txt

# Set default command
#CMD ["/usr/bin/bash"]
EXPOSE 3306
RUN systemctl start mysqld

