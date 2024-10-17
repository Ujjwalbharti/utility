FROM ubuntu:bionic

RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    curl \
    mysql-client \
    postgresql-client \
    redis-tools \
    wget \
    && rm -rf /var/lib/apt/lists/*