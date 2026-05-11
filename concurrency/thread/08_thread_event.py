"""
示例8: 线程事件（Event）
演示如何使用Event进行线程间的同步和通信
"""
import threading
import time

event = threading.Event()

def waiter():
    """等待线程：等待事件被触发"""
    print("  等待线程: 正在等待事件...")
    event.wait()  # 阻塞直到事件被设置
    print("  等待线程: 事件已触发!")

def setter():
    """设置线程：延迟后触发事件"""
    time.sleep(1)
    print("  设置线程: 正在设置事件...")
    event.set()

if __name__ == "__main__":
    print("=" * 50)
    print("示例8: 线程事件（Event）")
    print("=" * 50)
    print("演示线程间的同步和通信\n")
    
    # 创建等待线程和设置线程
    waiter_thread = threading.Thread(target=waiter, name="WaiterThread")
    setter_thread = threading.Thread(target=setter, name="SetterThread")
    
    # 启动线程
    waiter_thread.start()
    setter_thread.start()
    
    # 等待两个线程完成
    waiter_thread.join()
    setter_thread.join()
    
    print("\n✓ Event事件通信完成")
    print("=" * 50)
