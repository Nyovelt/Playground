from ubuntu:latest

RUN apt update && apt install -y python3 python3-pip perl && pip3 install requirements.txt && chmod +x ./moss/moss

CMD python3 main.py