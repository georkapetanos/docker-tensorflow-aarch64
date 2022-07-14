# syntax=docker/dockerfile:1

FROM --platform=linux/arm64 ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get -y install --no-install-recommends \
	build-essential \
	libhdf5-dev \
	libc-ares-dev \
	libeigen3-dev \
	gcc \
	gfortran \
	libgfortran5 \
	libatlas3-base \
	libatlas-base-dev \
	libopenblas-dev \
	libopenblas-base \
	libblas-dev \
	liblapack-dev \
	cython3 \
	libatlas-base-dev \
	openmpi-bin \
	openssh-server \
	libopenmpi-dev \
	python3-dev \
	python3 \
	python3-pip \
	wget
	
RUN pip3 install -U wheel mock six
RUN pip3 install --upgrade pip
RUN pip3 install protobuf==3.20.*

RUN wget https://github.com/PINTO0309/Tensorflow-bin/releases/download/v2.8.0/tensorflow-2.8.0-cp38-none-linux_aarch64.whl
RUN pip3 install /tensorflow-2.8.0-cp38-none-linux_aarch64.whl
RUN rm /tensorflow-2.8.0-cp38-none-linux_aarch64.whl
