# ARCHITECTURE_TESTS — BirthHub360 v12

| Regra / Decisão (ADR) | Fitness Function / Checklist de Pass-Fail |
| --------------------- | ----------------------------------------- |
| Nenhum módulo de domínio importa de infraestrutura (ADR-00X) | `import-linter` / script em bash (falhar se `grep "from infrastructure" src/domain`) |
| Todo arquivo Python de agente tem `AgentManifest` declarado | Script CI validando a classe instanciada / regex em arquivos em `/agents/*/src` |
| Nenhum secret hardcoded no código | TruffleHog / Gitleaks hook |
| Prisma schema tem campo `tenantId` em todas as tabelas multi-tenant (ADR-002) | Prisma schema AST validator (`grep -v tenantId schema.prisma` com whitelists) |
| Build completo < 5 minutos | CI Workflow duration rule |