# RUNBOOK_CICLO_0 — BirthHub360 v12

## Pré-requisitos
- Node 20+
- Python 3.11+
- Docker
- pnpm

## Setup
1. Instale as dependências: `pnpm install`
2. Gere o Prisma Client: `cd packages/database && npx prisma generate`
3. Inicie os serviços essenciais (Postgres, Redis): `docker-compose up -d`

## Como rodar os agentes Python
1. Vá até a pasta do agente: `cd agents/orchestrator`
2. Instale requisitos: `pip install -r requirements.txt`
3. Rode o serviço: `python src/main.py`

## Como rodar o Gateway
1. Vá até o gateway: `cd apps/gateway`
2. Rode em dev: `pnpm run dev`

## Troubleshooting comum
- Se o banco de dados falhar ao iniciar: Verifique se a porta 5432 já não está em uso (`lsof -i :5432`).
- Erro no gateway ao iniciar: Assegure que as dependências Typescript e o ts-node estão instalados e a versão do node é >=20.