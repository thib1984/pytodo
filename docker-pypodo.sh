#!/bin/bash

#if you modify theses values, stop and restart container with
#docker stop pypodo
#docker rm pypodo
PYPODO_FILE=~/.todo
PYPODO_BACKUP=~/.todo_backup
PYPODO_CONFIG=~/.todo.rc
PYPODO_FILE_CRYPT=~/.todo.crypt
PYPODO_FILE_DECRYPT=~/.todo.decrypt

touch $PYPODO_FILE
mkdir -p $PYPODO_BACKUP
touch $PYPODO_CONFIG
touch $PYPODO_FILE_CRYPT
touch $PYPODO_FILE_DECRYPT

#download image if it dooes not exist
docker images | grep "thibaultgarcon/pypodo:latest " >/dev/null || docker pull thibaultgarcon/pypodo:latest
#run the container if it dooes not run
docker ps | grep "pypodo " >/dev/null || docker run -d --rm --name "pypodo" --mount type=bind,source=${PYPODO_FILE},target=/root/.todo --mount type=bind,source=${PYPODO_FILE_DECRYPT},target=/root/.todo.decrypt --mount type=bind,source=${PYPODO_FILE_CRYPT},target=/root/.todo.crypt --mount type=bind,source=${PYPODO_CONFIG},target=/root/.todo.rc --mount type=bind,source=${PYPODO_BACKUP},target=/root/.todo_backup --entrypoint="sleep" thibaultgarcon/pypodo:latest 43200 > /dev/null

#prepa args
for x in "${@}" ; do
    # try to figure out if quoting was required for the $x
    if [[ "$x" != "${x%[[:space:]]*}" ]]; then
        x="\""$x"\""
    fi
    _args=$_args" "$x
done

#execute command
docker exec -ti pypodo sh -c "pypodo $_args"