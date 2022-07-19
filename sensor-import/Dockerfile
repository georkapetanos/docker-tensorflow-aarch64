# syntax=docker/dockerfile:1

FROM --platform=linux/arm64 ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install --no-install-recommends \
	python3 \
	python3-pip \
	kmod \
	i2c-tools \
	tzdata \
	nano
	
RUN pip3 install -U bmp280 smbus2 getmac

ENV UDEV=on
ENV TZ="Europe/Athens"
RUN ln -fs /usr/share/zoneinfo/Europe/Athens /etc/localtime && \
	dpkg-reconfigure -f noninteractive tzdata

COPY sensor_bmp.py /root/sensor.py
