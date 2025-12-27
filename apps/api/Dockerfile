FROM node:20-alpine

WORKDIR /app

# Install openssl for Prisma
RUN apk add --no-cache openssl

# Install pnpm
RUN npm install -g pnpm

# Since we are using workspaces, copying structure is a bit tricky in generic Dockerfiles without a build step in root.
# For local dev, we bind mount everything, so this Dockerfile is mostly for dependency installation cached layer.

COPY package.json pnpm-workspace.yaml pnpm-lock.yaml ./
# Copy only api package.json for install context
COPY apps/api/package.json ./apps/api/package.json

# Install dependencies (ignoring scripts to avoid postinstall issues initially)
RUN pnpm install --frozen-lockfile --ignore-scripts

COPY . .

# Generate Prisma Client
ARG DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb"
RUN DATABASE_URL="${DATABASE_URL}" pnpm -C apps/api prisma:generate

# In Dev, we override command normally, but here is a default
CMD ["pnpm", "-C", "apps/api", "start:dev"]
