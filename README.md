# calculator-api-challenge
Another implementation of calculator API using python's tornado framework.

Este pequeño servidor es de las respuestas enviadas al
[calculator API challenge](http://github.com/juanpabloaj/calculator-api-challenge)
organizado en el
[meetup de python de Viña del Mar](http://www.meetup.com/Python-Valparaiso-y-Vina-del-Mar).

## How to run
Está ideado para correr como una imagen [docker](http://www.docker.com). Para crear la imagen:

`docker build -t calculator-api-challenge .`

Para ejecutar la imagen, permitiendo llamadas al puerto en *localhost*:

`docker run -p 8888:8888 calculator-api-challenge`

## To Do
* Agregar test unitarios.
