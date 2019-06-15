FROM python
LABEL maintainer="Akira Shinohara <k017c1067@it-neec.jp>"

RUN apt-get update && apt-get install zsh git -y
RUN zsh -c 'git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"'
RUN zsh -c 'setopt EXTENDED_GLOB; for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do; ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"; done'

RUN mkdir /app
ADD ./src/ /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

