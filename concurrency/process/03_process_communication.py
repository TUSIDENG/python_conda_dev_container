"""
示例3: 进程间通信 (IPC)
演示如何使用Queue和Pipe进行进程间通信
"""
import multiprocessing
import time

def producer(queue):
    """生产者进程"""
    for i in range(5):
        item = f"产品-{i}"
        queue.put(item)
        print(f"  生产者进程: 生产了 {item}")
        time.sleep(0.3)
    
    # 发送结束信号
    queue.put(None)

def consumer(queue):
    """消费者进程"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"  消费者进程: 消费了 {item}")
        time.sleep(0.5)

if __name__ == "__main__":
    print("=" * 50)
    print("示例3: 进程间通信 (IPC)")
    print("=" * 50)
    print("使用Queue进行进程间通信\n")
    
    # 创建队列
    queue = multiprocessing.Queue()
    
    # 创建生产者和消费者进程
    producer_process = multiprocessing.Process(
        target=producer,
        args=(queue,),
        name="Producer"
    )
    
    consumer_process = multiprocessing.Process(
        target=consumer,
        args=(queue,),
        name="Consumer"
    )
    
    # 启动进程
    producer_process.start()
    consumer_process.start()
    
    # 等待进程完成
    producer_process.join()
    consumer_process.join()
    
    print("\n✓ 进程间通信完成")
    print("=" * 50)
