# UBIQUITOUS_LANGUAGE — BirthHub360 v12

### Tenant
**Definição:** Organização cliente isolada na plataforma BirthHub360. Cada tenant tem seu próprio conjunto de dados, agentes e configurações sem visibilidade cross-tenant.
**Sinônimos proibidos:** cliente, empresa, org (usar sempre "tenant" no código)
**Bounded Context:** TenantManagement, presente em todos os outros contexts como referência
**Tipo no código:** `TenantContext` (packages/shared/src/types/index.ts)

### Agent
**Definição:** Entidade de software Python responsável por processar lógicas complexas e de IA baseada em regras de domínio.
**Sinônimos proibidos:** script, robô, bot.
**Bounded Context:** AgentRuntime

### AgentManifest
**Definição:** Arquivo descritivo ou contrato que declara dependências, versão e capacidades de um agente.
**Sinônimos proibidos:** config, specs.
**Bounded Context:** AgentRuntime
**Tipo no código:** `AgentManifest`

### Execution
**Definição:** A instância executável e estado de processamento de um Agent.
**Bounded Context:** AgentRuntime
**Tipo no código:** `AgentExecution`

### Pack
**Definição:** Conjunto de Skills e capacidades agrupadas oferecidas no Marketplace.
**Sinônimos proibidos:** pacote, bundle.
**Bounded Context:** Marketplace

### Skill
**Definição:** Unidade de conhecimento ou operação específica que um Agent pode executar (ex: Ler PDF Médico).
**Bounded Context:** Marketplace / AgentRuntime

### Pipeline
**Definição:** A trilha organizada de execuções de vários Agentes formando um fluxo.
**Sinônimos proibidos:** workflow, job.
**Bounded Context:** AgentRuntime

### Orchestrator
**Definição:** O agente principal que coordena a execução de outros agentes baseados no grafo de dependências (Topological Sort).
**Bounded Context:** AgentRuntime

### Gateway
**Definição:** Ponto de entrada das requisições externas para o sistema, lidando com middleware e rotas básicas antes do repasse aos serviços.
**Bounded Context:** Gateway (API API Layer)

### Subscription
**Definição:** O contrato ativo que um Tenant possui para acessar funcionalidades e Packs na plataforma.
**Bounded Context:** Billing

### Plan
**Definição:** Um conjunto agrupado de permissões, SLAs e precificação aplicável a uma Subscription.
**Bounded Context:** Billing

### Cycle
**Definição:** O ciclo de desenvolvimento ou faturamento na arquitetura BirthHub360.

### Phase
**Definição:** Agrupamento de tarefas ou estágios dentro de um Cycle.

### Item
**Definição:** Unidade discreta de trabalho a ser executada e avaliada por agentes.

### ADR
**Definição:** Architecture Decision Record, documento vivo sobre decisões arquiteturais.
**Bounded Context:** Governance

### FitnessFunction
**Definição:** Script ou teste que avalia automaticamente a aderência da arquitetura a um ADR ou NFR.
**Bounded Context:** Governance

### BoundedContext
**Definição:** Limite explícito de um subdomínio dentro do projeto onde a linguagem e regras são consistentes.
**Bounded Context:** Architecture

### Aggregate
**Definição:** Raiz de um cluster de entidades de domínio tratadas como uma única unidade de dados persistidos.
**Bounded Context:** Architecture

### DomainEvent
**Definição:** Acontecimento de relevância para especialistas de domínio registrado pela plataforma.
**Bounded Context:** Architecture

### QueueAdapter
**Definição:** Interface de software para publicação e subscrição de mensagens assíncronas entre serviços.
**Bounded Context:** Infrastructure