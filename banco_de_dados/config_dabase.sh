# Script start MariaDB docker

sudo docker run -e MARIADB_ROOT_PASSWORD=password -v </path/mysql>:/var/lib/mysql -d mariadb
                   MARIADB_ALLOW_EMPTY_ROOT_PASSWORD 
# Docker 

sudo docker inspect <id>

sudo docker exec -it <id> bash

sudo docker container rm <id> --force

sudo docker container ls

sudo docker images