"""
示例2: 多个并发线程
演示如何创建和管理多个线程并发执行
"""
import threading
import time

def worker(worker_id):
    """工作线程函数"""
    for i in range(3):
        print(f"  工作线程 {worker_id}: 任务 {i}")
        time.sleep(0.3)

if __name__ == "__main__":
    start_time = time.time()

    print("=" * 50)
    print("示例2: 多个并发线程")
    print("=" * 50)
    
    threads = []
    
    # 创建3个工作线程
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,), name=f"Worker-{i}")
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    print("✓ 所有线程执行完成")
    print("=" * 50)

    exec_time = time.time() - start_time
    print(f"总耗时: {exec_time:.2f} 秒")
