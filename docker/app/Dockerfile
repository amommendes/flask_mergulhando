FROM scratch
ADD centos-7-x86_64-docker.tar.xz /

LABEL org.label-schema.schema-version="1.0" \
    org.label-schema.name="CentOS Base Image" \
    org.label-schema.vendor="CentOS" \
    org.label-schema.license="GPLv2" \
    org.label-schema.build-date="20190305"

RUN yum update -y
RUN yum install -y yum-utils wget curl vim jq git
RUN wget https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update -y
RUN ls -lrt *.rpm
RUN yum install -y ius-release.rpm
RUN yum install -y mysql

# Install Python3.6 and pip
RUN yum install -y python36u
RUN yum install -y python36u-pip
RUN pip3.6 install --upgrade pip
RUN python3.6 -V
RUN pip3.6 -V

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

ARG CACHEBUST=1
COPY ./app /app
COPY ./requirements.txt /app

WORKDIR /app

RUN touch /app/guinicorn_access.log 
RUN touch /app/guinicorn_error.log

# Installing Dependencies
RUN pip3.6 install -r requirements.txt
EXPOSE 5000

RUN echo "0.0.0.0   localhost" >> /etc/hosts

CMD ["sh", "/app/start_app.sh" ]
