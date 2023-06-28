FROM redis:7.0.2

LABEL maintainer="minjong@viasoft.ai"
LABEL version="1.0.0"
LABEL date="2023.06.28"
LABEL description="django channels redis"

COPY redis.conf /usr/local/etc/redis/redis.conf
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]