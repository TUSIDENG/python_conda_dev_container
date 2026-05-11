"""
示例1: 基础线程创建和启动
演示如何创建和启动简单的线程
"""
import threading
import time

def print_numbers():
    """打印数字的线程函数"""
    for i in range(3):
        print(f"  线程: 数字 {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    print("=" * 50)
    print("示例1: 基础线程创建和启动")
    print("=" * 50)
    start_time = time.time()
    # 创建线程
    thread = threading.Thread(target=print_numbers, name="PrintThread")
    
    # 启动线程
    thread.start()
    
    # 等待线程完成
    thread.join()
    
    print("✓ 线程执行完成")
    print("=" * 50)
    end_time = time.time()

    print(f"总耗时: {end_time - start_time:.2f} 秒")
