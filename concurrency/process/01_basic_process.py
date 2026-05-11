"""
示例1: 基础进程创建和启动
演示如何创建和启动简单的进程
"""
import multiprocessing
import time

def calculate(n):
    """计算任务：计算前n个自然数的平方和"""
    result = sum(i * i for i in range(n))
    print(f"  进程 {multiprocessing.current_process().name}: 计算完成，结果={result}")
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("示例1: 基础进程创建和启动")
    print("=" * 50)
    
    # 创建进程
    process = multiprocessing.Process(
        target=calculate,
        args=(1000000,),
        name="CalcProcess"
    )
    
    # 启动进程
    print(f"  主进程 {multiprocessing.current_process().name}: 启动子进程")
    process.start()
    
    # 等待进程完成
    process.join()
    
    print("  主进程: 子进程已完成")
    print("✓ 进程执行完成")
    print("=" * 50)
