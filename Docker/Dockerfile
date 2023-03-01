FROM cr.msk.sbercloud.ru/aicloud-base-images/horovod-cuda11.1-pt1.9.1-a100:0.0.28

USER root

WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive

COPY requirements.txt .

RUN pip install -r requirements.txt
