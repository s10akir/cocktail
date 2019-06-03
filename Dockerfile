FROM python
LABEL maintainer="Akira Shinohara <k017c1067@it-neec.jp>"

RUN pip install django
RUN mkdir /app
RUN apt-get update && apt-get install zsh git -y
RUN zsh -c 'git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"'
RUN zsh -c 'setopt EXTENDED_GLOB; for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do; ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"; done'

EXPOSE 8000

WORKDIR /app
