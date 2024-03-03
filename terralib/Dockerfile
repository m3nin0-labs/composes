FROM ubuntu:18.04

ENV TERRALIB_DOWNLOAD_URL="www.dpi.inpe.br/terralib5/download/download.php?FileName=terralib-5.5.0-ubuntu-18.04.tar.gz"

RUN apt update -y >> /dev/null && \
    apt install wget tar sudo build-essential -y >> /dev/null && \ 
    wget ${TERRALIB_DOWNLOAD_URL} -O terralib-X.X.X-ubuntu.tar.gz && \
    mkdir terralib && tar -vzxf terralib-X.X.X-ubuntu.tar.gz -C terralib && \
    cd terralib && chmod +x install.sh && ./install.sh

ENTRYPOINT [ "/bin/bash" ]
