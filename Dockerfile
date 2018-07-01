FROM python:3.5

WORKDIR /meetup/
COPY ./ /meetup/
RUN pip3 install -r requirements.txt
