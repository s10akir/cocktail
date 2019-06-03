FROM python
LABEL maintainer="Akira Shinohara <k017c1067@it-neec.jp>"

RUN pip install django
RUN mkdir /app

EXPOSE 8000

WORKDIR /app
