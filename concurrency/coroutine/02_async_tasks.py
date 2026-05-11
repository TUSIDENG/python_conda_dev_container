"""
示例2: 异步任务创建
演示如何使用asyncio.create_task创建和管理异步任务
"""
import asyncio
import time

async def worker(worker_id, delay):
    """异步工作函数"""
    print(f"  工作线程 {worker_id}: 开始工作")
    await asyncio.sleep(delay)
    print(f"  工作线程 {worker_id}: 完成工作")
    return f"结果-{worker_id}"

async def main():
    """主协程：创建和管理多个任务"""
    print("=" * 50)
    print("示例2: 异步任务创建")
    print("=" * 50)
    
    print("\n使用create_task创建任务...\n")
    start_time = time.time()
    
    # 创建多个异步任务
    task1 = asyncio.create_task(worker(1, 1))
    task2 = asyncio.create_task(worker(2, 2))
    task3 = asyncio.create_task(worker(3, 1.5))
    task4 = asyncio.create_task(worker(4, 0.5))
    
    # 等待所有任务完成并获取结果
    results = await asyncio.gather(task1, task2, task3, task4)
    
    elapsed = time.time() - start_time
    
    print(f"\n结果: {results}")
    print(f"✓ 所有任务完成，耗时: {elapsed:.2f}秒")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main())
