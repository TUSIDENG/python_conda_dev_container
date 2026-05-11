"""
示例6: 生产者-消费者模式
演示如何使用Queue实现生产者-消费者的线程间通信
"""
import threading
import time
from queue import Queue

queue = Queue(maxsize=3)  # 创建容量为3的队列

def producer():
    """生产者线程"""
    for i in range(5):
        item = f"产品-{i}"
        queue.put(item)
        print(f"  生产者: 生产了 {item}")
        time.sleep(0.3)

def consumer():
    """消费者线程"""
    while True:
        item = queue.get()
        if item is None:  # None 作为结束信号
            break
        print(f"  消费者: 消费了 {item}")
        time.sleep(0.5)
        queue.task_done()

if __name__ == "__main__":
    print("=" * 50)
    print("示例6: 生产者-消费者模式")
    print("=" * 50)
    print("队列容量: 3\n")
    
    # 创建生产者和消费者线程
    producer_thread = threading.Thread(target=producer, name="Producer")
    consumer_thread = threading.Thread(target=consumer, name="Consumer")
    
    # 启动线程
    producer_thread.start()
    consumer_thread.start()
    
    # 等待生产者完成
    producer_thread.join()
    
    # 发送结束信号给消费者
    queue.put(None)
    
    # 等待消费者完成
    consumer_thread.join()
    
    print("\n✓ 生产者-消费者模式完成")
    print("=" * 50)
