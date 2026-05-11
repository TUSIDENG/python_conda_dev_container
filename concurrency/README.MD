# Python 并发编程：进程 vs 线程 vs 协程

## 概述

Python提供三种主要的并发编程方式：进程、线程和协程。每种方式都有其独特的特点和适用场景。

---

## 1. 基本概念对比

| 特性 | 进程(Process) | 线程(Thread) | 协程(Coroutine) |
|------|--------------|-----------|-----------------|
| **创建开销** | 大 | 中等 | 很小 |
| **内存占用** | 大（独立内存空间） | 中等（共享内存） | 很小 |
| **切换开销** | 大（OS切换） | 中等（OS调度） | 小（用户态） |
| **并发能力** | 真正并发 | 受GIL限制* | 高效任务切换 |
| **难度** | 难（进程间通信复杂） | 中（需要同步机制） | 易（顺序编程风格） |
| **GIL影响** | 无 | 有** | 无 |
| **适用场景** | CPU密集型 | I/O密集型 | I/O密集型(异步) |

*Python GIL(全局解释器锁)：同一时刻只有一个线程执行Python字节码
**线程无法真正并行执行CPU密集任务

---

## 2. 进程 (Process)

### 特点
- **独立内存空间**：每个进程有自己完整的Python解释器和内存空间
- **真正并发**：不受GIL限制，真正的并行执行
- **进程隔离**：一个进程的崩溃不影响其他进程
- **开销大**：创建和切换成本高

### 适用场景
- CPU密集型计算（数据处理、科学计算等）
- 需要利用多核CPU的场景
- 进程之间完全独立的任务

### 创建方式
```python
from multiprocessing import Process

def cpu_task(n):
    result = sum(i*i for i in range(n))
    return result

if __name__ == '__main__':
    process = Process(target=cpu_task, args=(1000000,))
    process.start()
    process.join()
```

---

## 3. 线程 (Thread)

### 特点
- **共享内存空间**：同一进程内的线程共享内存
- **轻量级**：比进程更轻，创建成本较低
- **GIL限制**：同一时刻只有一个线程执行Python代码
- **线程安全问题**：需要同步机制保护共享资源

### 适用场景
- I/O密集型任务（网络请求、文件读写等）
- 需要共享数据的并发任务
- 简单的并发需求

### 创建方式
```python
import threading

def io_task():
    # 模拟I/O操作
    time.sleep(1)

thread = threading.Thread(target=io_task)
thread.start()
thread.join()
```

### 同步机制
- **Lock（互斥锁）**：保护共享资源
- **RLock（递归锁）**：支持同一线程多次获取
- **Semaphore（信号量）**：限制并发数量
- **Event（事件）**：线程间通信
- **Condition（条件变量）**：复杂的线程间协调

---

## 4. 协程 (Coroutine)

### 特点
- **轻量级**：成千上万的协程可以在一个线程中运行
- **高效**：基于事件循环，用户态切换，成本极低
- **单线程**：避免了多线程的复杂性和竞态条件
- **异步I/O**：天然支持异步操作

### 适用场景
- 大量I/O并发的场景（网络爬虫、Web服务器等）
- 需要处理数万个并发连接的应用
- 不需要共享状态的独立任务

### 创建方式
```python
import asyncio

async def io_task():
    await asyncio.sleep(1)

# 运行协程
asyncio.run(io_task())
```

---

## 5. 性能对比

### CPU密集型任务
```
进程 > 串行 >> 线程 >>> 协程
（进程利用多核，线程受GIL限制，协程单线程不适合）
```

### I/O密集型任务
```
协程 > 线程 >> 进程 >>> 串行
（协程成本最低，线程次之，进程开销太大）
```

### 内存占用
```
协程 << 线程 < 进程
（协程最轻量，1000000个协程可行，线程1000+就很难）
```

---

## 6. 文件结构

```
concurrency/
├── threading01.py           # 综合线程示例
├── thread/                  # 线程示例目录
│   ├── 01_basic_thread.py
│   ├── 02_concurrent_threads.py
│   ├── 03_thread_lock.py
│   ├── 04_semaphore.py
│   ├── 05_thread_pool.py
│   ├── 06_producer_consumer.py
│   ├── 07_daemon_thread.py
│   └── 08_thread_event.py
├── process/                 # 进程示例目录
│   ├── 01_basic_process.py
│   ├── 02_process_pool.py
│   ├── 03_process_communication.py
│   └── 04_shared_memory.py
├── coroutine/               # 协程示例目录
│   ├── 01_basic_coroutine.py
│   ├── 02_async_tasks.py
│   ├── 03_async_io.py
│   └── 04_async_gather.py
└── comparison/              # 对比示例
    ├── cpu_intensive.py     # CPU密集型对比
    ├── io_intensive.py      # I/O密集型对比
    └── memory_usage.py      # 内存占用对比
```

---

## 7. 选择指南

### 使用进程 (Process) 当：
- ✅ 执行CPU密集型计算
- ✅ 需要真正的并行处理
- ✅ 任务间完全独立
- ✅ 需要隔离和容错

### 使用线程 (Thread) 当：
- ✅ I/O密集型任务
- ✅ 需要共享数据
- ✅ 并发数量不太大（<1000）
- ✅ 不需要异步编程的复杂性

### 使用协程 (Coroutine) 当：
- ✅ 大量并发I/O操作
- ✅ 需要处理数千个并发连接
- ✅ 编写异步代码，如Web框架
- ✅ 网络爬虫、API调用等

---

## 8. 关键差异总结

### 并发能力
- **进程**：多个进程可以在多个CPU核上并行执行
- **线程**：同一时间只有一个线程执行Python代码（GIL限制）
- **协程**：一个线程内的多个协程通过事件循环实现高效调度

### 内存模型
- **进程**：完全独立，进程间通信需要特殊机制
- **线程**：共享内存，需要同步机制保护
- **协程**：栈分离，通过await实现控制权传递

### 编程模型
- **进程**：最接近OS级别的并发
- **线程**：多线程编程容易出现竞态条件
- **协程**：代码看起来像同步，实际是异步

---

## 9. 示例运行

### 线程示例
```bash
python thread/01_basic_thread.py
python thread/03_thread_lock.py
python thread/05_thread_pool.py
```

### 进程示例
```bash
python process/01_basic_process.py
python process/02_process_pool.py
```

### 协程示例
```bash
python coroutine/01_basic_coroutine.py
python coroutine/02_async_tasks.py
```

### 性能对比
```bash
python comparison/cpu_intensive.py    # CPU密集型对比
python comparison/io_intensive.py     # I/O密集型对比
python comparison/memory_usage.py     # 内存占用对比
```

---

## 10. 最佳实践

1. **优先考虑协程** - 对于I/O密集型任务，协程是首选
2. **CPU密集任务用进程** - 不要用线程做CPU密集工作
3. **避免过度并发** - 不是并发度越高越好
4. **正确使用同步机制** - 线程中保护共享资源
5. **监控资源** - 进程和线程都要留意内存和CPU
6. **异步优先** - 新项目优先考虑async/await

