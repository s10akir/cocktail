FROM python
LABEL maintainer="Akira Shinohara <k017c1067@it-neec.jp>"

RUN pip install django
RUN useradd -m cocktail
RUN mkdir /app && chown cocktail:cocktail /app

EXPOSE 8000

WORKDIR /app
