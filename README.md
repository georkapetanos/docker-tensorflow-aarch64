Tensorflow 2.8 on ubuntu 20.04 for AArch64 (arm64)

docker compose build --progress=plain
balena push myFleet
#docker build --platform linux/arm64 --progress=plain --tag docker-tensorflow-aarch64 .
balena-engine exec -it <container_id> /bin/sh

docker run -it docker-tensorflow-aarch64 s
