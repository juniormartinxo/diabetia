# Usando uma imagem base do Redis
FROM redis:7.4.0-alpine

# Diretório de trabalho dentro do container
WORKDIR /usr/local/etc/redis

# Copia a configuração personalizada para dentro do container
COPY redis.conf /usr/local/etc/redis/redis.conf

# Cria diretórios de logs e dados
RUN mkdir -p /var/log/redis /var/lib/redis/data

# Expõe a porta padrão do Redis
EXPOSE 6379

# Comando padrão para iniciar o Redis com configuração customizada
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]