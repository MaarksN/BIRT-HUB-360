import asyncio
import time
from planner import AsyncMemoryPool

async def run_benchmark(pool, iterations):
    start_time = time.perf_counter()
    for i in range(iterations):
        key = f"key_{i}"
        await pool.set(key, i)
        await pool.get(key)
    end_time = time.perf_counter()
    return end_time - start_time

async def main():
    iterations = 100000
    pool = AsyncMemoryPool()

    # Warmup
    await run_benchmark(pool, 1000)

    duration = await run_benchmark(pool, iterations)
    print(f"Total time for {iterations} ops: {duration:.4f} seconds")
    print(f"Average time per op: {(duration / iterations) * 1e6:.4f} microseconds")

if __name__ == "__main__":
    asyncio.run(main())
