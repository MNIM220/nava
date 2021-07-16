#!/bin/bash

if [ $1 == "uwsgi" ]; then
    shift
    /usr/bin/uwsgi --uid www-data --gid www-data --buffer-size=32768 --plugins=python3 --chdir=/var/www --socket=0.0.0.0:9000 --callable app $@ &
    wait

elif [ $1 == "sh" ]; then
    sh

fi
