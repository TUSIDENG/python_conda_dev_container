"""
示例4: asyncio.gather和异常处理
演示如何使用gather并发执行多个协程，以及处理异常
"""
import asyncio
import time
import random

async def async_operation(op_id, delay=None):
    """异步操作"""
    if delay is None:
        delay = random.uniform(0.5, 2)
    
    print(f"  操作 {op_id}: 开始 (预期耗时 {delay:.1f}秒)")
    await asyncio.sleep(delay)
    
    # 模拟随机失败
    if random.random() < 0.2:  # 20%概率失败
        raise Exception(f"操作 {op_id} 失败")
    
    print(f"  操作 {op_id}: 完成")
    return f"操作{op_id}结果"

async def main_with_gather():
    """使用gather并发执行"""
    print("=" * 50)
    print("示例4: asyncio.gather 和异常处理")
    print("=" * 50)
    
    print("\n方式1: gather(return_exceptions=False) - 第一个异常停止\n")
    
    tasks = [async_operation(i) for i in range(1, 4)]
    
    try:
        results = await asyncio.gather(*tasks)
        print(f"\n结果: {results}")
    except Exception as e:
        print(f"\n捕获到异常: {e}")
    
    print("\n" + "-" * 50)
    print("方式2: gather(return_exceptions=True) - 继续执行，返回异常\n")
    
    tasks = [async_operation(i) for i in range(4, 7)]
    
    # return_exceptions=True 时，异常也会作为结果返回
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    print("\n结果和异常混合:")
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"  {i}. 异常: {result}")
        else:
            print(f"  {i}. {result}")
    
    print("\n✓ gather示例完成")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main_with_gather())
