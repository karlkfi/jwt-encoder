FROM alpine:3.10

RUN apk --no-cache add --update \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
    libffi-dev \
    openssl-dev \
  && pip3 install --upgrade pip \
  && pip3 install PyJWT \
  && pip3 install cryptography \
  && pip3 install click \
  && apk del build-base python3-dev py3-pip libffi-dev openssl-dev \
  && rm -rf /var/cache/apk/*

WORKDIR /

COPY ./jwt-encoder.py /

ENTRYPOINT ["./jwt-encoder.py"]
