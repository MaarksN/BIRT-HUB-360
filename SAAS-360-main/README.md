# BirthHub360 SaaS Platform

Bem-vindo ao monorepo oficial do **BirthHub360**, uma plataforma SaaS especializada baseada em múltiplos agentes Python e infraestrutura TypeScript.

## Visão Geral
Este repositório contém:
- **apps/**: Aplicações voltadas para o usuário (como o `web` frontend) e pontos de entrada (como o API `gateway`).
- **packages/**: Pacotes compartilhados, incluindo utilitários TypeScript, banco de dados (`database`) e esquema Prisma, garantindo consistência.
- **agents/**: O core inteligente. Uma frota de agentes Python (ex: `orchestrator`, `agente_1`) gerenciando a complexidade do domínio.
- **docs/**: Nossa base de conhecimento, incluindo `governance` arquitetural, Decisões de Arquitetura (ADRs) e Runbooks.

## Primeiros Passos
Consulte o [RUNBOOK_CICLO_0](docs/governance/runbooks/RUNBOOK_CICLO_0.md) para instalar e executar as ferramentas necessárias.