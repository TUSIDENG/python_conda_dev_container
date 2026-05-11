"""
示例7: 守护线程 (Daemon Thread)
演示守护线程的特性：主线程退出时，守护线程也会被终止
"""
import threading
import time

def daemon_worker():
    """守护线程函数"""
    for i in range(10):
        print(f"  守护线程: 工作 {i}")
        time.sleep(0.2)

def main_worker():
    """主线程函数"""
    for i in range(3):
        print(f"  主线程: 工作 {i}")
        time.sleep(0.3)

if __name__ == "__main__":
    print("=" * 50)
    print("示例7: 守护线程 (Daemon Thread)")
    print("=" * 50)
    
    # 创建守护线程
    daemon_thread = threading.Thread(
        target=daemon_worker, 
        daemon=True, 
        name="DaemonThread"
    )
    
    # 创建普通线程
    normal_thread = threading.Thread(
        target=main_worker,
        name="NormalThread"
    )
    
    # 启动线程
    daemon_thread.start()
    normal_thread.start()
    
    # 等待普通线程完成
    normal_thread.join()
    
    print("  主线程: 主线程继续执行...")
    time.sleep(0.5)
    
    print("\n✓ 守护线程示例完成")
    print("  注: 守护线程会在主线程退出时被终止")
    print("=" * 50)
