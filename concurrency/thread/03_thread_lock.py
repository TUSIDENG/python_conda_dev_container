"""
示例3: 线程同步 - Lock（互斥锁）
演示如何使用Lock保证线程安全的共享资源访问
"""
import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter(thread_id):
    """增加计数器的线程函数"""
    global counter
    for _ in range(1000):
        # 使用Lock保护共享资源
        with counter_lock:
            counter += 1

if __name__ == "__main__":
    print("=" * 50)
    print("示例3: 线程同步 - Lock（互斥锁）")
    print("=" * 50)
    
    threads = []
    
    # 创建3个线程，每个线程对计数器增加1000
    for i in range(3):
        t = threading.Thread(target=increment_counter, args=(i,))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    print(f"最终计数器值: {counter}")
    print(f"预期值: 3000")
    print(f"✓ 使用Lock保证线程安全")
    print("=" * 50)
