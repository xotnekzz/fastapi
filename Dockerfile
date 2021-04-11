FROM ubuntu:20.04

#apt로 패키지설치시 프롬프트를 방지하기 위한 Args
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

#apt repo 최신화 
RUN apt update

#add-apt-repository 커맨드 설치용
RUN apt-get install -y software-properties-common

#필요한 패키지 설치
RUN apt-get install -y vim git wget sqlite3 unzip bc locales && \
    apt-get install -y rsyslog supervisor && \
    apt-get install -y python3-dev build-essential libcairo2-dev libjpeg-dev libgif-dev

#pip 설치
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip setuptools wheel 

#한글 locale 설정
RUN locale-gen ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

#NGINX 설치
RUN apt-get install -y nginx
RUN addgroup nginx && \
    useradd -g nginx nginx 

# CODE
RUN git clone https://github.com/xotnekzz/fastapi.git /var/www/fastapi
WORKDIR /var/www/fastapi
RUN git remote update
RUN mkdir /home/nginx
RUN chown -R nginx.nginx /home/nginx

RUN git pull origin main

RUN pip install -r /var/www/fastapi/config/requirements.txt

EXPOSE 80

RUN cd /var/www/fastapi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]
