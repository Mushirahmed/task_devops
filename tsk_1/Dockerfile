FROM centos:centos6

MAINTAINER Mushirahmed <imushir@gmail.com>

# For installing dependencies
RUN yum -y update && \
    yum install -y \
    bzip2-devel \
    git \
    hostname \
    openssl \
    apr-devel \
    openssl-devel \
    sqlite-devel \
    sudo \
    tar \
    wget \
    gcc \
    zlib-dev

# Install python2.7
RUN yum install -y centos-release-scl && \
    yum install -y python27 && \
    scl enable python27 bash

# Install mongoDB v 2.4 
RUN yum install -y mongodb24 && \
    scl enable mongodb24 bash    

# Install Tomcat 7
RUN wget "http://apache.mirrors.spacedump.net/tomcat/tomcat-7/v7.0.73/bin/apache-tomcat-7.0.73.tar.gz" -O apache-tomcat-7.0.73.tar.gz && \
	tar xvzf apache-tomcat-7.0.73.tar.gz && \
    mv apache-tomcat-7.0.73 /usr/local/tomcat7

#Starting services

CMD ["/etc/init.d/mongodb24-mongodb" , "start" ]
CMD ["/usr/local/tomcat7/bin/catalina.sh" , "run"]

# Expose ports for tomcat and mongodb
EXPOSE 7080 8080
EXPOSE 27017 27017

 
