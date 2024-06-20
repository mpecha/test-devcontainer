FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG user=default_user

### Install software ###
RUN apt update

RUN apt install -y sudo
RUN apt install -y git

RUN apt install -y python3
RUN apt install -y python3-pip && ln -sf python3 /usr/bin/python

### Install python packages ###
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install --no-cache numpy

### Install other required packages ###
RUN apt install -y libxext-dev
RUN apt install -y libxrender-dev
RUN apt install -y libxtst-dev
RUN apt install -y libxi-dev
RUN apt install -y libfreetype-dev
RUN apt install -y procps

### Create user ###
RUN useradd --create-home --shell=/bin/bash $user
RUN adduser $user $user
RUN echo "$user:$user" | chpasswd

RUN usermod -aG sudo $user
RUN echo "$user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

### Set home directory permissions ###
RUN chown -R $user:$user /home/$user

### Final setup ###
USER $user
WORKDIR /home/$user
