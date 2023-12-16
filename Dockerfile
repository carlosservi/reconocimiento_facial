FROM python:3.10-slim

LABEL version="1.0" \
      maintainer="carlosservi@correo.ugr.es"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    unzip \
    pkg-config \
    python3-dev \
    python3-opencv \
    libjpeg-dev \
    zlib1g-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libtiff5-dev \
    libatlas-base-dev \
    libfreetype6-dev \
    libwebp-dev \
    libffi-dev

# Install dlib
RUN git clone -b 'v19.22' --single-branch https://github.com/davisking/dlib.git \
    && cd dlib \
    && python3 setup.py install \
    && cd .. \
    && rm -rf dlib

# Crea la carpeta "Data" y define un volumen para persistir los datos
VOLUME /usr/src/app/Data

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app

CMD ["python3", "main.py"]
