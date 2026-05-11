"""
示例3: 异步I/O操作
演示如何进行异步网络请求和I/O操作
"""
import asyncio
import time

async def fetch_data(url, delay):
    """模拟异步获取数据"""
    print(f"  开始请求: {url}")
    # 模拟网络延迟
    await asyncio.sleep(delay)
    print(f"  完成请求: {url}")
    return f"数据来自 {url}"

async def concurrent_requests():
    """并发发送多个请求"""
    print("=" * 50)
    print("示例3: 异步I/O操作")
    print("=" * 50)
    
    urls = [
        ("http://api.example.com/data1", 1),
        ("http://api.example.com/data2", 0.8),
        ("http://api.example.com/data3", 1.2),
        ("http://api.example.com/data4", 0.5),
        ("http://api.example.com/data5", 0.9),
    ]
    
    print("\n使用asyncio.gather并发请求...\n")
    start_time = time.time()
    
    # 创建所有请求任务
    tasks = [fetch_data(url, delay) for url, delay in urls]
    
    # 并发执行所有请求
    results = await asyncio.gather(*tasks)
    
    elapsed = time.time() - start_time
    
    print(f"\n获取的数据:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")
    
    print(f"\n✓ 所有请求完成，耗时: {elapsed:.2f}秒")
    print(f"  (顺序执行需要 {sum(d for _, d in urls):.1f}秒)")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(concurrent_requests())
