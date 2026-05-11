"""
示例4: 共享内存
演示如何在进程间共享数据：Value和Array
"""
import multiprocessing
import time

def increment_counter(counter, lock):
    """增加共享计数器"""
    for _ in range(100):
        with lock:
            counter.value += 1

def modify_array(arr, index, value, lock):
    """修改共享数组"""
    with lock:
        arr[index] = value
    print(f"  进程: 修改数组[{index}] = {value}")

if __name__ == "__main__":
    print("=" * 50)
    print("示例4: 进程间共享内存")
    print("=" * 50)
    
    # 创建共享变量和锁
    counter = multiprocessing.Value('i', 0)  # 共享整数，初始值0
    lock = multiprocessing.Lock()  # 进程级别的锁
    
    # 创建和启动多个进程来增加计数器
    processes = []
    print("\n1. 共享计数器示例\n")
    
    for i in range(3):
        p = multiprocessing.Process(
            target=increment_counter,
            args=(counter, lock)
        )
        processes.append(p)
        p.start()
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print(f"  最终计数器值: {counter.value}")
    print(f"  预期值: 300\n")
    
    # 共享数组示例
    print("2. 共享数组示例\n")
    
    shared_array = multiprocessing.Array('i', [0, 0, 0, 0, 0])
    lock = multiprocessing.Lock()
    
    processes = []
    for i in range(5):
        p = multiprocessing.Process(
            target=modify_array,
            args=(shared_array, i, i*10, lock)
        )
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"\n  最终数组: {list(shared_array)}")
    
    print("\n✓ 共享内存示例完成")
    print("=" * 50)
