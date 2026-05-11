"""
对比3: 内存占用对比
对比进程、线程、协程的内存占用情况
"""
import threading
import multiprocessing
import asyncio
import psutil
import os
import sys

def dummy_function():
    """空函数，用于线程和进程中执行"""
    import time
    time.sleep(10)

def measure_memory(label, create_func, count):
    """测量指定数量的对象内存占用"""
    print(f"\n{label}")
    print("-" * 40)
    
    process = psutil.Process(os.getpid())
    
    # 获取初始内存
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    print(f"  初始内存: {initial_memory:.2f} MB")
    
    try:
        # 创建指定数量的对象
        objects = []
        for i in range(count):
            obj = create_func()
            objects.append(obj)
        
        # 获取创建后的内存
        current_memory = process.memory_info().rss / 1024 / 1024  # MB
        used_memory = current_memory - initial_memory
        per_object = used_memory * 1024 / count  # KB per object
        
        print(f"  创建{count}个对象后: {current_memory:.2f} MB")
        print(f"  占用内存: {used_memory:.2f} MB")
        print(f"  平均每个: {per_object:.2f} KB")
        
        # 清理对象
        if isinstance(objects[0], threading.Thread):
            for obj in objects:
                if obj.is_alive():
                    pass  # 线程无法直接关闭
        
        objects.clear()
        
    except Exception as e:
        print(f"  错误: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("对比3: 内存占用对比")
    print("=" * 60)
    
    # 检查是否安装了psutil
    try:
        import psutil
    except ImportError:
        print("请先安装psutil: pip install psutil")
        sys.exit(1)
    
    # 小数量对比
    print("\n小规模对比 (创建10个对象)")
    print("=" * 60)
    
    # 线程对比
    def create_thread():
        return threading.Thread(target=dummy_function)
    
    measure_memory("1. 线程 (10个线程)", create_thread, 10)
    
    # 协程对比
    async def dummy_coroutine():
        await asyncio.sleep(10)
    
    def create_coroutine():
        return dummy_coroutine()
    
    measure_memory("2. 协程 (10个协程)", create_coroutine, 10)
    
    # 进程对比 (只创建2个，因为开销大)
    def create_process():
        return multiprocessing.Process(target=dummy_function)
    
    measure_memory("3. 进程 (2个进程)", create_process, 2)
    
    # 大规模对比
    print("\n\n大规模对比 (创建1000个对象)")
    print("=" * 60)
    
    print("\n1. 线程 (1000个线程) - 通常会失败")
    print("-" * 40)
    try:
        threads = []
        for i in range(1000):
            t = threading.Thread(target=dummy_function)
            threads.append(t)
        print(f"  成功创建1000个线程")
        process = psutil.Process(os.getpid())
        memory = process.memory_info().rss / 1024 / 1024
        print(f"  当前内存占用: {memory:.2f} MB")
    except Exception as e:
        print(f"  失败: {e}")
    
    print("\n2. 协程 (1000000个协程) - 可行")
    print("-" * 40)
    print("  创建1000000个协程...")
    try:
        coros = [dummy_coroutine() for _ in range(1000000)]
        process = psutil.Process(os.getpid())
        memory = process.memory_info().rss / 1024 / 1024
        print(f"  成功创建1000000个协程")
        print(f"  当前内存占用: {memory:.2f} MB")
        print(f"  平均每个协程: {(memory * 1024 / 1000000):.3f} KB")
        coros.clear()
    except Exception as e:
        print(f"  失败: {e}")
    
    print("\n" + "=" * 60)
    print("总结")
    print("=" * 60)
    print("""
内存占用排序（从小到大）:
  1. 协程: 最轻量级，一个进程可运行数百万个协程
  2. 线程: 中等，一个进程通常最多支持数千个线程
  3. 进程: 最重，独立内存空间，创建成本很高

具体数据:
  - 线程: 平均每个线程占用 1-10 MB
  - 协程: 平均每个协程占用 < 1 KB
  - 进程: 平均每个进程占用 30-50 MB

建议:
  ✓ 需要大量并发: 优先使用协程
  ✓ 简单I/O并发: 使用线程
  ✓ CPU密集或隔离: 使用进程
    """)
    print("=" * 60)
