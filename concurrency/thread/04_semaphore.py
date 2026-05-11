"""
示例4: 信号量（Semaphore）
演示如何使用Semaphore限制对共享资源的并发访问数量
"""
import threading
import time

semaphore = threading.Semaphore(2)  # 同时只允许2个线程访问

def limited_resource(resource_id):
    """访问有限资源的线程函数"""
    with semaphore:
        print(f"  资源 {resource_id}: 获得访问权限")
        time.sleep(0.5)
        print(f"  资源 {resource_id}: 释放访问权限")

if __name__ == "__main__":
    print("=" * 50)
    print("示例4: 信号量（Semaphore）")
    print("=" * 50)
    print("同时只允许2个线程访问资源\n")
    
    threads = []
    
    # 创建5个线程尝试访问有限资源
    for i in range(5):
        t = threading.Thread(target=limited_resource, args=(i,))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    print("\n✓ 信号量限制并发访问完成")
    print("=" * 50)
