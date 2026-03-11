export interface AgentManifest {
  id: string;
  name: string;
  version: string;
  capabilities: string[];
}

export interface ExecutionResult {
  id: string;
  status: 'PENDING' | 'RUNNING' | 'SUCCESS' | 'FAILED';
  output?: any;
  error?: string;
  duration_ms?: number;
}

export interface TenantContext {
  tenantId: string;
  roles: string[];
}

export interface PlanNode {
  id: string;
  dependencies: string[];
  status: 'PENDING' | 'READY' | 'COMPLETED' | 'BLOCKED';
}