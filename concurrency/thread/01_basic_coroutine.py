"""
协程示例1: 基础异步函数
对应线程示例1，演示async/await的基础用法
"""
import asyncio

async def print_numbers():
    """异步打印数字的协程函数"""
    for i in range(3):
        print(f"  协程: 数字 {i}")
        await asyncio.sleep(0.5)

async def main():
    print("=" * 50)
    print("协程示例1: 基础异步函数")
    print("=" * 50)
    
    # 直接await执行协程
    await print_numbers()
    
    print("✓ 协程执行完成")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main())
