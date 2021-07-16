FROM ubuntu:16.04

MAINTAINER Nima Hashemi "nima.hashemy@gmail.com"

# Install System requirnment pakcages
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data && \
        apt-get update && apt-get install -y python3 python3-pip python3-dev uwsgi uwsgi-plugin-python3 \
        ca-certificates vim curl libmysqlclient-dev libffi-dev libssl-dev && ln -s /usr/bin/pip3 /usr/bin/pip && mkdir /var/www && rm -rf /var/cache/apt/*

RUN apt install -y iputils-ping

# Copy requirenments
COPY ["entrypoint.sh", "requirements.txt", "/"]

# Install python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY [".", "/var/www"]

RUN apt-get autoremove --purge -y python3-dev gcc && \
        chmod +x /entrypoint.sh && chown -R www-data. /var/www

WORKDIR "/var/www"

ENTRYPOINT ["/entrypoint.sh"]