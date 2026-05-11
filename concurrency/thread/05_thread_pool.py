"""
示例5: 线程池 (ThreadPoolExecutor)
演示如何使用ThreadPoolExecutor管理线程池执行任务
"""
import time
from concurrent.futures import ThreadPoolExecutor

def square(n):
    """计算数字的平方"""
    time.sleep(0.2)
    result = n * n
    print(f"  计算 {n}² = {result}")
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("示例5: 线程池 (ThreadPoolExecutor)")
    print("=" * 50)
    
    numbers = [1, 2, 3, 4, 5]
    
    # 使用ThreadPoolExecutor创建线程池，最多3个工作线程
    with ThreadPoolExecutor(max_workers=3) as executor:
        print(f"输入数字: {numbers}\n")
        
        # 使用map方法批量提交任务
        results = executor.map(square, numbers)
        
        # 获取结果
        result_list = list(results)
    
    print(f"\n平方结果: {result_list}")
    print("✓ 线程池执行完成")
    print("=" * 50)
