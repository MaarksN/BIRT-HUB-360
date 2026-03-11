import express, { Request, Response, NextFunction } from 'express';

const app = express();
app.use(express.json());

// Tenant middleware
const tenantMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const tenantId = req.headers['x-tenant-id'];
  if (!tenantId) {
    return res.status(401).json({ error: 'x-tenant-id header is required' });
  }
  // @ts-ignore
  req.tenantContext = { tenantId, roles: [] };
  next();
};

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', service: 'gateway' });
});

app.use('/agents', tenantMiddleware);
app.get('/agents', (req, res) => {
  res.json({ agents: ['orchestrator', 'agente_1'] });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Gateway running on port ${PORT}`);
});