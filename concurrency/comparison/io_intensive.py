"""
对比2: I/O密集型任务性能对比
对比进程、线程、协程在I/O密集型任务中的性能
"""
import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def io_task(task_id, delay):
    """I/O密集型任务：模拟网络请求"""
    print(f"  进程/线程 {task_id}: 开始I/O操作")
    time.sleep(delay)  # 模拟I/O等待
    print(f"  进程/线程 {task_id}: 完成I/O操作")
    return f"结果-{task_id}"

# ===== 方式1: 串行执行 =====
def serial_execution(task_count, delay):
    """串行执行I/O任务"""
    start = time.time()
    results = []
    for i in range(task_count):
        results.append(io_task(i, delay))
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式2: 多线程执行 =====
def thread_execution(task_count, delay):
    """使用线程执行I/O任务"""
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(io_task, i, delay) for i in range(task_count)]
        results = [f.result() for f in futures]
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式3: 多进程执行 =====
def process_execution(task_count, delay):
    """使用进程执行I/O任务"""
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(io_task, [(i, delay) for i in range(task_count)])
    elapsed = time.time() - start
    return results, elapsed

# ===== 方式4: 异步执行 =====
async def async_io_task(task_id, delay):
    """异步I/O任务"""
    print(f"  协程 {task_id}: 开始I/O操作")
    await asyncio.sleep(delay)  # 异步等待
    print(f"  协程 {task_id}: 完成I/O操作")
    return f"结果-{task_id}"

async def async_execution(task_count, delay):
    """使用协程执行I/O任务"""
    start = time.time()
    tasks = [async_io_task(i, delay) for i in range(task_count)]
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start
    return results, elapsed

if __name__ == "__main__":
    print("=" * 60)
    print("对比2: I/O密集型任务性能对比")
    print("=" * 60)
    print("任务: 模拟10个网络请求，每个延迟1秒\n")
    
    task_count = 10
    io_delay = 1  # 每个任务的I/O延迟
    
    print("1. 串行执行")
    print("-" * 40)
    print("  执行10个串行I/O任务...")
    results, serial_time = serial_execution(task_count, io_delay)
    print(f"  耗时: {serial_time:.2f}秒\n")
    
    print("2. 多线程执行 (4个线程)")
    print("-" * 40)
    print("  执行10个I/O任务，使用4个线程...")
    results, thread_time = thread_execution(task_count, io_delay)
    print(f"  耗时: {thread_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/thread_time:.2f}倍\n")
    
    print("3. 多进程执行 (4个进程)")
    print("-" * 40)
    print("  执行10个I/O任务，使用4个进程...")
    results, process_time = process_execution(task_count, io_delay)
    print(f"  耗时: {process_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/process_time:.2f}倍\n")
    
    print("4. 异步协程执行")
    print("-" * 40)
    print("  执行10个I/O任务，使用异步协程...")
    results, async_time = asyncio.run(async_execution(task_count, io_delay))
    print(f"  耗时: {async_time:.2f}秒")
    print(f"  性能对比串行: {serial_time/async_time:.2f}倍\n")
    
    print("=" * 60)
    print("性能排序（从快到慢）:")
    times = [
        ("协程", async_time),
        ("多线程", thread_time),
        ("多进程", process_time),
        ("串行", serial_time),
    ]
    times.sort(key=lambda x: x[1])
    for i, (method, t) in enumerate(times, 1):
        print(f"  {i}. {method:8} - {t:6.2f}秒")
    
    print("\n结论:")
    print("  ✓ I/O密集型: 协程 > 多线程 ≥ 多进程 >> 串行")
    print("  原因:")
    print("    - 协程: 用户态切换，成本最低，I/O等待时自动切换")
    print("    - 线程: OS级调度，成本较高，但仍能并发I/O")
    print("    - 进程: 创建和切换成本高，不适合轻量级I/O任务")
    print("=" * 60)
