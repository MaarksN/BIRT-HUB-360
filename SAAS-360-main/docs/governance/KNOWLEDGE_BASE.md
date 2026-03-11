# Knowledge Base — BirthHub360 v12

## Ciclo 0 — Aprendizados

### Padrões que funcionaram
- Estrutura clara monorepo Turborepo com apps e packages otimizou a base de código TypeScript.
- Abstrações Python desacopladas da camada HTTP permitiram fácil integração do Orchestrator.

### Anti-padrões evitados
- Evitar dependências diretas de agents na API base. O AGENT_REGISTRY garante desacoplamento de build.
- Evitar schemas descentralizados: Prisma é a Single Source of Truth para o DB Postgres.

### Decisões arquiteturais não formalizadas como ADR
- A adoção do TypeScript 5+ ao invés de versões mais antigas para utilizar melhor recursos restritos do compilador `skipLibCheck: true`.