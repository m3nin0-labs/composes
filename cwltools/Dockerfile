FROM ubuntu@sha256:2f4a6ca7bdf2a532473610a46b2900e94c9c987925bff20603ba087ac6d919f7

RUN apt-get update && apt-get install -y python3-dev python3-pip curl \
    && pip3 install pip --upgrade \
    && pip3 install cwltool cwl-runner

RUN curl -fsSL https://get.docker.com -o get-docker.sh \
	&& sh get-docker.sh

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
