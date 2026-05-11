"""
示例2: 进程池 (Pool)
演示如何使用进程池管理多个进程执行任务
"""
import multiprocessing
import time

def cpu_task(n):
    """CPU密集型任务：计算第n个斐波那契数列"""
    def fib(num):
        if num <= 1:
            return num
        return fib(num - 1) + fib(num - 2)
    
    result = fib(n)
    print(f"  fib({n}) = {result}")
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("示例2: 进程池 (Pool)")
    print("=" * 50)
    
    numbers = [30, 31, 32, 33, 34]
    
    # 创建进程池，包含4个工作进程
    with multiprocessing.Pool(processes=4) as pool:
        print(f"  计算斐波那契数列: {numbers}\n")
        start_time = time.time()
        
        # 使用map方法批量提交任务
        results = pool.map(cpu_task, numbers)
        
        elapsed = time.time() - start_time
    
    print(f"\n  结果: {results}")
    print(f"  耗时: {elapsed:.2f}秒")
    print("✓ 进程池执行完成")
    print("=" * 50)
