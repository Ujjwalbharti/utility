FROM ubuntu:bionic

RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    curl \
    mysql-client \
    postgresql-client \
    redis-tools \
    wget \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*