FROM ubuntu:22.04
LABEL RUN="docker run -it --name NAME --privileged --ipc=host --net=host --pid=host -e HOST=/host -e NAME=NAME -e IMAGE=IMAGE -v /run:/run -v /var/log:/var/log -v /etc/localtime:/etc/localtime -v /:/host IMAGE"
# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
RUN apt-get update && \
    apt-get install -y \
    wget \
    lsb-release \
    gnupg \
    ca-certificates \
    python3 \
    git \
    nginx \
    python3-pip \
    python3.10-venv \
    docker.io \
    && wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb \
    && dpkg -i mysql-apt-config_0.8.17-1_all.deb \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C \
    && apt-get update \
    && apt-get install -y mysql-client=8.0* \
    && rm -rf /var/lib/apt/lists/* \
    && rm mysql-apt-config_0.8.17-1_all.deb
RUN useradd -d /home/ifotos -ms /bin/bash ifotos
USER ifotos
RUN cd && git clone https://github.com/ifriedman7/IFotos.git
WORKDIR /home/ifotos/IFotos
RUN /usr/bin/pip3 install -r requirements.txt

# Set default command
#CMD ["/usr/bin/bash"]
EXPOSE 3000
ENTRYPOINT [ "python3", "app.py" ]
#ENTRYPOINT [ "uwsgi", "--ini", "uwsgi-IFotos.ini" ]

