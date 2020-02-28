docker kill chrome isenmesez csrf_isenmesez ;

docker run -d --rm --network='host' --name chrome selenium/standalone-chrome:3.141.59-zirconium && \
docker run -d --rm --network='host' --name isenmesez fenchelfen/isenmesez:latest && \
docker run -d --rm --network='host' --name csrf_isenmesez fenchelfen/csrf_isenmesez:latest
