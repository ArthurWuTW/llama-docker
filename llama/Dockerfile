FROM nvidia/cuda:12.1.0-cudnn8-devel-rockylinux8

RUN yum install -y ncurses
RUN yum install -y python3.12 python3.12-pip
RUN pip3.12 install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
RUN yum install -y libnccl libnccl-devel libnccl-static

RUN pip3.12 install six
