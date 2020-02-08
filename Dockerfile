FROM python:3.7-alpine

RUN mkdir /srv/src
WORKDIR /srv/src

ADD requirements.txt /srv/src/

RUN \
 pip install --upgrade pip setuptools && \
 pip install -r requirements.txt

ADD sites/cookbook /srv/src/sites/cookbook
ADD sites/sites /srv/src/sites/sites
ADD sites/manage.py /srv/src/sites/manage.py

EXPOSE 12345

ENTRYPOINT ["python", "sites/manage.py", "runserver", "0.0.0.0:12345"]
