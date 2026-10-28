# Multi-Stage Production Dockerfile for Skill.Sea
# Ultra-compact, secure, runs with unprivileged user on port 8080

FROM node:20-alpine AS runner

WORKDIR /app

# Set production environment
ENV NODE_ENV=production
ENV PORT=8080
ENV HOST=0.0.0.0

# Copy application files
COPY package.json server.js index.html ./
COPY styles/ ./styles/
COPY src/ ./src/
COPY data/ ./data/
COPY scripts/ ./scripts/

# Set ownership to unprivileged node user
RUN chown -R node:node /app

USER node

EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1

CMD ["node", "server.js"]
