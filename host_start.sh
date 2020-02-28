docker kill chrome isenmesez csrf_isenmesez ;

docker run -d --rm --network='host' --name chrome selenium/standalone-chrome:3.141.59-zirconium && \
docker run -d --rm --network='host' --name isenmesez isenmesez:latest && \
docker run -d --network='host' --name csrf_isenmesez csrf_isenmesez:latest
