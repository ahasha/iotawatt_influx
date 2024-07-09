#!/bin/bash
mkdir -p $PWD/influx.db

docker run --rm --name=influxdb -d -p 8086:8086 \
      -e INFLUXDB_DB=iotawatt \
      -e INFLUXDB_HTTP_AUTH_ENABLED=true \
      -e INFLUXDB_ADMIN_USER=admin -e INFLUXDB_ADMIN_PASSWORD=abc123 \
      -v $PWD/influx.db:/var/lib/influxdb \
      influxdb
