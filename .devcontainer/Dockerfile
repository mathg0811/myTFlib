FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

# tzdata 같은 패키지가 터미널 입력 안 기다리게 설정
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.9 python3.9-dev python3-pip \
    git build-essential curl \
    && rm -rf /var/lib/apt/lists/*

RUN python3.9 -m pip install --upgrade pip cython

WORKDIR /workspace

COPY requirements.txt /workspace/requirements.txt
RUN python3.9 -m pip install -r requirements.txt
