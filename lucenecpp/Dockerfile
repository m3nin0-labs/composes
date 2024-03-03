FROM rocker/geospatial:4.3.2

WORKDIR /app

RUN apt update -y \
    && apt install -y \
    && apt install \
        git \
        cmake \
        zlib1g-dev \
        libboost-date-time-dev \
        libboost-filesystem-dev \
        libboost-regex-dev \
        libboost-thread-dev \
        libboost-iostreams-dev -y \
    && apt autoclean \
    && apt autoremove

RUN git clone https://github.com/luceneplusplus/LucenePlusPlus.git \
    && cd LucenePlusPlus \
    && mkdir build; cd build \
    && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make \
    && make install \
    && cd /app \
    && rm -rf LucenePlusPlus
