# ADR-002-multi-tenancy-row-level-security.md

- Decisão: Row-Level Security (RLS) no Postgres como estratégia de isolamento
- Contexto: SaaS multi-tenant com dados sensíveis de saúde materno-infantil
- Consequências: tenantId obrigatório em todas as queries, middleware de contexto