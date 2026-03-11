import asyncio
import unittest
from planner import AsyncMemoryPool, build_plan, topological_sort, DependencyCycleError

class TestAsyncMemoryPool(unittest.IsolatedAsyncioTestCase):
    async def test_get_set(self):
        pool = AsyncMemoryPool()
        await pool.set("key1", "value1")
        self.assertEqual(await pool.get("key1"), "value1")
        self.assertIsNone(await pool.get("key2"))

    async def test_concurrent_access(self):
        pool = AsyncMemoryPool()
        async def set_val(i):
            await pool.set(f"key{i}", i)

        await asyncio.gather(*(set_val(i) for i in range(100)))

        for i in range(100):
            self.assertEqual(await pool.get(f"key{i}"), i)

class TestTopologicalSort(unittest.TestCase):
    def test_simple_sort(self):
        graph = {
            "A": {"B"},
            "B": set(),
            "C": {"A", "B"}
        }
        # C depends on A, B. A depends on B. B depends on nothing.
        # Order: [B], [A], [C]
        result = topological_sort(graph)
        self.assertEqual(result, [["B"], ["A"], ["C"]])

    def test_cycle_detection(self):
        graph = {
            "A": {"B"},
            "B": {"A"}
        }
        with self.assertRaises(DependencyCycleError):
            topological_sort(graph)

if __name__ == "__main__":
    unittest.main()
