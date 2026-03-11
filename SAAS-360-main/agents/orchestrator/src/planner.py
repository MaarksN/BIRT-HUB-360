from collections import deque, defaultdict
from typing import Dict, List, Set
from registry import get_registry
import asyncio

class DependencyCycleError(Exception):
    pass

def build_plan():
    registry = get_registry()
    graph = {name: set(info.get("depends_on", [])) for name, info in registry.items()}
    return topological_sort(graph)

def topological_sort(graph: Dict[str, Set[str]]) -> List[List[str]]:
    """
    Returns groups of parallel-executable nodes.
    Raises DependencyCycleError if a cycle is detected.
    """
    in_degree = {u: 0 for u in graph}
    adj = defaultdict(list)

    for u, deps in graph.items():
        for dep in deps:
            if dep not in graph:
                graph[dep] = set()
                in_degree[dep] = 0
            adj[dep].append(u)
            in_degree[u] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    groups = []

    visited_count = 0
    while queue:
        level_size = len(queue)
        current_group = []
        for _ in range(level_size):
            u = queue.popleft()
            current_group.append(u)
            visited_count += 1

            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        groups.append(current_group)

    if visited_count != len(in_degree):
        raise DependencyCycleError("Dependency cycle detected")

    return groups

class AsyncMemoryPool:
    def __init__(self):
        self._pool = {}

    async def get(self, key: str):
        return self._pool.get(key)

    async def set(self, key: str, value: any):
        self._pool[key] = value