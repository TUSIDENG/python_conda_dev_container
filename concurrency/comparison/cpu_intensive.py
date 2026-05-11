"""
对比1: CPU密集型任务性能对比
对比进程、线程、协程在CPU密集型任务中的性能
"""
import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def cpu_task(n):
    """CPU密集型任务：计算第n个斐波那契数列"""
    def fib(num):
        if num <= 1:
            return num
        return fib(num - 1) + fib(num - 2)
    return fib(n)

# ===== 方式1: 串行执行 =====
def serial_execution(tasks):
    """串行执行任务"""
    start = time.time()
    results = [cpu_task(n) for n in tasks]
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式2: 多线程执行 =====
def thread_execution(tasks):
    """使用线程执行任务"""
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_task, tasks))
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式3: 多进程执行 =====
def process_execution(tasks):
    """使用进程执行任务"""
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_task, tasks)
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式4: 异步执行（对于CPU任务效果不佳）=====
async def async_cpu_task(n):
    """异步CPU任务（实际上没有真正异步）"""
    return cpu_task(n)

async def async_execution(tasks):
    """使用协程执行任务"""
    start = time.time()
    coros = [async_cpu_task(n) for n in tasks]
    results = await asyncio.gather(*coros)
    elapsed = time.time() - start
    return results, elapsed

if __name__ == "__main__":
    print("=" * 60)
    print("对比1: CPU密集型任务性能对比")
    print("=" * 60)
    print("任务: 计算斐波那契数列\n")
    
    # CPU密集型任务
    tasks = [32, 32, 32, 32]
    
    print("1. 串行执行")
    print("-" * 40)
    results, serial_time = serial_execution(tasks)
    print(f"  结果: {results}")
    print(f"  耗时: {serial_time:.2f}秒\n")
    
    print("2. 多线程执行")
    print("-" * 40)
    results, thread_time = thread_execution(tasks)
    print(f"  结果: {results}")
    print(f"  耗时: {thread_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/thread_time:.2f}倍\n")
    
    print("3. 多进程执行")
    print("-" * 40)
    results, process_time = process_execution(tasks)
    print(f"  结果: {results}")
    print(f"  耗时: {process_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/process_time:.2f}倍\n")
    
    print("4. 异步协程执行")
    print("-" * 40)
    results, async_time = asyncio.run(async_execution(tasks))
    print(f"  结果: {results}")
    print(f"  耗时: {async_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/async_time:.2f}倍\n")
    
    print("=" * 60)
    print("性能排序（从快到慢）:")
    times = [
        ("多进程", process_time),
        ("串行", serial_time),
        ("多线程", thread_time),
        ("协程", async_time),
    ]
    times.sort(key=lambda x: x[1])
    for i, (method, t) in enumerate(times, 1):
        print(f"  {i}. {method:8} - {t:6.2f}秒")
    
    print("\n结论:")
    print("  ✓ CPU密集型：多进程 > 串行 >> 多线程 ≈ 协程")
    print("  原因: 多进程利用多核，线程受GIL限制，协程无法并行")
    print("=" * 60)
