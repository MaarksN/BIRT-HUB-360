AGENT_REGISTRY = {
    "orchestrator": {"depends_on": []},
    "agente_1": {"depends_on": ["orchestrator"]},
}

def get_registry():
    return AGENT_REGISTRY