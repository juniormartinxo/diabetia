# Diabetia - Infraestrutura Local

Este repositório contém o monorepo do projeto **Diabetia**, configurado com Docker Compose para desenvolvimento local.

## Estrutura do Monoretório

```
diabetia/
├── apps/
│   ├── api/        # NestJS API + Prisma
│   ├── crawler/    # Python Crawler Worker
│   └── embedder/   # Python Embedder Worker
├── infra/
│   └── docker-compose.yml
├── packages/       # Pacotes compartilhados (estrutura inicial)
├── docker-compose.yml
└── README.md
```

## Pré-requisitos

- Docker & Docker Compose plugin
- (Opcional) pnpm instalado localmente para visualizar código/intellisense

## Como Rodar

1. Certifique-se de que o Docker está rodando.
2. Na raiz do projeto, execute:
   ```bash
   npm run dev
   # OU
   docker compose -f infra/docker-compose.yml up -d --build
   ```

3. O sistema irá:
   - Subir o Postgres (com extensão `pgvector`) e Redis.
   - Rodar o container `migrate` para aplicar as migrações do Prisma (Schema + SQL nativo para vetores).
   - Iniciar a API, Crawler e Embedder.

## Serviços e Portas

| Serviço  | URL Interna | Porta Host | Descrição |
|----------|-------------|------------|-----------|
| API      | `api`       | 3000       | NestJS API (Swagger em /api) |
| Postgres | `postgres`  | -          | Banco de Dados (user: postgres, pass: postgres, db: diabetia) |
| Redis    | `redis`     | -          | Cache e Fila |
| Adminer  | `adminer`   | 8080       | Interface Web para o Banco de Dados |

## Verificação e Health Checks

- **API Health**: acesse [http://localhost:3000/health](http://localhost:3000/health). Deve retornar `OK`.
- **Swagger**: acesse [http://localhost:3000/api](http://localhost:3000/api).
- **Logs**:
  ```bash
  docker compose -f infra/docker-compose.yml logs -f
  ```

## Desenvolvimento

- **API**: O código em `apps/api` está mapeado via volume. Alterações no código irão disparar o Hot Reload (NestJS).
- **Prisma Migrations**:
  - As migrações estão em `apps/api/prisma/migrations`.
  - A migração inicial (`0_init`) contém o SQL raw para habilitar `vector` e criar índices `HNSW`.
  - Para criar novas migrações (requer dependências locais instaladas ou rodar via container):
    ```bash
    pnpm -C apps/api prisma migrate dev
    ```

## Comandos Úteis

```bash
# Derrubar a stack
npm run down

# Ver logs da API
docker compose -f infra/docker-compose.yml logs -f api

# Acessar shell do Postgres
docker compose -f infra/docker-compose.yml exec postgres psql -U postgres -d diabetia
```

## Checklist de Validação

1. [ ] `docker ps` mostra todos os containers `healthy` ou `Up`.
2. [ ] `http://localhost:3000/health` retorna 200 OK.
3. [ ] `docker compose logs migrate` mostra `Database schema is now in sync with it.`.
4. [ ] Conectar no Banco (via Adminer localhost:8080) e verificar se a tabela `ChunkEmbedding` tem a coluna `embedding` do tipo `vector`.
