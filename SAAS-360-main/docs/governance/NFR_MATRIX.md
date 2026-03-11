# NFR_MATRIX — BirthHub360 v12

| ID | Requisito | Categoria | SLA | ADR | Teste de Verificação | Owner |
|----|-----------|-----------|-----|-----|---------------------|-------|
| NFR-001 | Latência de API | Performance | P95 < 200ms | ADR-001 | k6 load test | CODEX |
| NFR-002 | Isolamento de tenant | Segurança | 100% isolamento | ADR-002 | Integration test | JULES |
| NFR-003 | Disponibilidade Geral | Disponibilidade | 99.9% uptime | ADR-00X | Pingdom/Datadog monitors | CODEX |
| NFR-004 | Throughput Agentes | Performance | 100 req/s | ADR-005 | k6 / Locust em `orchestrator` | JULES |
| NFR-005 | Tempo de Recuperação | Confiabilidade | RTO < 4 horas | ADR-00X | Chaos Engineering drill | CODEX |
| NFR-006 | Auditoria de Segurança | Rastreabilidade | 100% logs mantidos 90d | ADR-002 | AWS CloudTrail check | JULES |
| NFR-007 | Cobertura de Testes | Manutenibilidade | > 80% código | ADR-00X | SonarQube | CODEX |
| NFR-008 | Atualização de Schema | Manutenibilidade | Zero-downtime migs | ADR-004 | CI migration dry-run | JULES |
| NFR-009 | Limite de Conexões | Confiabilidade | < 80% cap. banco | ADR-004 | PgBouncer metrics | CODEX |
| NFR-010 | Compatibilidade Browsers| Usabilidade | Últimas 2 ver. | ADR-00X | Playwright cross-browser | JULES |