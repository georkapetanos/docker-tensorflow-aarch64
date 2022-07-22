## Docker multicontainer setup for importing, processing and publishing data from sensors on BalenaOS device

### Services

- sensor-import: Python script for importing BMP280 sensor data and publishing to RabbitMQ server  
- tensowflow: Tensorflow 2.8 on ubuntu 20.04 for AArch64 (arm64)

### Setup used

* Raspberry Pi 4 (running balenaOS 2.98.33 64-bit)
* GY-BMP280-3.3 Atmospheric pressure (and temperature) sensor module, connected over I<sup>2</sup>C bus
* Server running RabbitMQ 3.8.2 in an unprivileged container
