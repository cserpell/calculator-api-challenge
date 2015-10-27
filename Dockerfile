FROM buildpack-deps:jessie
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y update && apt-get install -y build-essential python python-dev python-virtualenv
RUN mkdir /src
WORKDIR /src
COPY server.py requirements.txt ./
RUN virtualenv ve
RUN . ve/bin/activate && pip install -r requirements.txt
EXPOSE 8888
CMD . ve/bin/activate && python server.py
