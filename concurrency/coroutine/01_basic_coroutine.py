"""
示例1: 基础协程
演示如何创建和执行基础协程
"""
import asyncio
import time

async def say_hello(name, delay):
    """异步函数：延迟后问候"""
    print(f"  协程 {name}: 开始执行")
    await asyncio.sleep(delay)  # 异步等待
    print(f"  协程 {name}: 完成执行 (延迟了 {delay}秒)")

async def main():
    """主协程"""
    print("=" * 50)
    print("示例1: 基础协程")
    print("=" * 50)
    
    # 创建协程任务
    coro1 = say_hello("Task1", 1)
    coro2 = say_hello("Task2", 2)
    coro3 = say_hello("Task3", 1.5)
    
    # 并发执行多个协程
    print("\n开始执行协程...\n")
    start_time = time.time()
    
    await asyncio.gather(coro1, coro2, coro3)
    
    elapsed = time.time() - start_time
    print(f"\n✓ 所有协程完成，耗时: {elapsed:.2f}秒")
    print("=" * 50)

if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main())
