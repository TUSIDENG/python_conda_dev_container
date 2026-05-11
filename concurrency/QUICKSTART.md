# 快速参考指南

## 📁 项目结构

```
concurrency/
├── README.MD                    # 完整的理论对比文档
├── threading01.py               # 综合线程示例
│
├── thread/                       # 线程示例
│   ├── 01_basic_thread.py        # 基础线程
│   ├── 02_concurrent_threads.py  # 并发线程
│   ├── 03_thread_lock.py         # Lock互斥锁
│   ├── 04_semaphore.py           # 信号量
│   ├── 05_thread_pool.py         # 线程池
│   ├── 06_producer_consumer.py   # 生产者-消费者
│   ├── 07_daemon_thread.py       # 守护线程
│   └── 08_thread_event.py        # 事件通信
│
├── process/                      # 进程示例
│   ├── 01_basic_process.py       # 基础进程
│   ├── 02_process_pool.py        # 进程池
│   ├── 03_process_communication.py # 进程间通信
│   └── 04_shared_memory.py       # 共享内存
│
├── coroutine/                    # 协程示例
│   ├── 01_basic_coroutine.py     # 基础协程
│   ├── 02_async_tasks.py         # 异步任务
│   ├── 03_async_io.py            # 异步I/O
│   └── 04_async_gather.py        # gather和异常处理
│
└── comparison/                   # 对比示例
    ├── cpu_intensive.py          # CPU密集型对比
    ├── io_intensive.py           # I/O密集型对比
    ├── memory_usage.py           # 内存占用对比
    └── comprehensive_comparison.py # 综合对比指南
```

---

## 🚀 快速开始

### 学习线程
```bash
# 基础线程概念
python concurrency/thread/01_basic_thread.py

# 多个线程并发
python concurrency/thread/02_concurrent_threads.py

# 线程同步
python concurrency/thread/03_thread_lock.py

# 线程池
python concurrency/thread/05_thread_pool.py
```

### 学习进程
```bash
# 基础进程
python concurrency/process/01_basic_process.py

# 进程池
python concurrency/process/02_process_pool.py

# 进程通信
python concurrency/process/03_process_communication.py
```

### 学习协程
```bash
# 基础协程
python concurrency/coroutine/01_basic_coroutine.py

# 异步任务
python concurrency/coroutine/02_async_tasks.py

# 异步I/O
python concurrency/coroutine/03_async_io.py
```

### 性能对比
```bash
# CPU密集型对比
python concurrency/comparison/cpu_intensive.py

# I/O密集型对比
python concurrency/comparison/io_intensive.py

# 内存占用对比（需要psutil）
pip install psutil
python concurrency/comparison/memory_usage.py

# 综合对比指南
python concurrency/comparison/comprehensive_comparison.py
```

---

## 🎯 快速决策指南

### 选择合适的并发方式

| 场景 | 推荐方式 | 理由 |
|------|--------|------|
| 处理>1000个并发I/O | **协程** | 最轻量，成本最低 |
| CPU密集计算 | **进程** | 利用多核，避免GIL |
| 简单I/O并发(<1000) | **线程** | 简单易用 |
| 网络爬虫 | **协程** | 高效处理大量连接 |
| 数据处理 | **进程** | 充分利用多核 |
| Web框架异步 | **协程** | 原生async/await支持 |

### 性能排序

**CPU密集型:**
```
多进程 > 串行 >> 多线程 ≈ 协程
```

**I/O密集型:**
```
协程 > 多线程 ≥ 多进程 >> 串行
```

**内存占用:**
```
协程 << 线程 < 进程
```

---

## 📊 对比总表

```
┌────────┬─────────────┬─────────────┬─────────────┐
│ 特性   │   进程      │   线程      │   协程      │
├────────┼─────────────┼─────────────┼─────────────┤
│ 开销   │ 很大        │ 中等        │ 很小        │
│ 内存   │ 大          │ 中          │ 很小        │
│ 切换   │ 大(OS)      │ 中(OS)      │ 小(用户)    │
│ 数量   │ 数十-百     │ 百-千       │ 百万        │
│ GIL    │ 无          │ 有          │ 无          │
│ 安全   │ 天然隔离    │ 需要同步    │ 单线程      │
│ 通信   │ 队列/管道   │ 共享+锁     │ 消息传递    │
│ 难度   │ 高          │ 中          │ 低          │
└────────┴─────────────┴─────────────┴─────────────┘
```

---

## 💡 关键概念

### GIL (Global Interpreter Lock)
- Python线程受到GIL限制，同一时刻只有一个线程执行Python字节码
- CPU密集任务中，多线程反而比单线程慢
- 进程和协程不受GIL限制

### asyncio 事件循环
- 协程通过事件循环实现非阻塞I/O
- `await` 关键字让出控制权，允许其他协程执行
- 一个线程管理数百万个协程

### 进程间通信 (IPC)
- Queue: 线程安全的队列，进程间通信
- Pipe: 管道，点对点通信
- Value/Array: 共享内存变量
- Manager: 高级共享数据结构

---

## 🔧 常用模式

### 生产者-消费者模式
```python
# 线程版本
from queue import Queue
queue = Queue()
# 生产者放入数据
queue.put(data)
# 消费者取出数据
data = queue.get()

# 进程版本
from multiprocessing import Queue
queue = Queue()  # 进程级别队列

# 协程版本
import asyncio
queue = asyncio.Queue()
await queue.put(data)
data = await queue.get()
```

### 并发执行任务
```python
# 线程池
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(func, items)

# 进程池
from multiprocessing import Pool
with Pool(processes=4) as pool:
    results = pool.map(func, items)

# 协程
async def main():
    tasks = [func(item) for item in items]
    results = await asyncio.gather(*tasks)
asyncio.run(main())
```

### 线程同步
```python
# Lock (互斥锁)
lock = threading.Lock()
with lock:
    # 临界区代码

# Semaphore (信号量)
sem = threading.Semaphore(2)
with sem:
    # 最多2个线程同时执行

# Event (事件)
event = threading.Event()
event.wait()   # 等待
event.set()    # 设置
```

---

## 📚 学习路径

### 初级 (入门理解)
1. 读 README.MD 理论部分
2. 运行 `comprehensive_comparison.py` 了解概全貌
3. 学习各个基础示例 (01_xxx.py)

### 中级 (深入应用)
1. 学习同步机制 (Lock, Semaphore, Event)
2. 学习池 (ThreadPool, ProcessPool)
3. 学习生产者-消费者模式

### 高级 (实战优化)
1. 运行性能对比脚本
2. 根据具体场景选择合适方案
3. 处理异常和资源清理
4. 监控内存和CPU占用

---

## ⚠️ 注意事项

1. **线程安全**: 多线程访问共享资源必须使用锁
2. **资源泄漏**: 确保线程/进程/协程正确结束
3. **异常处理**: 并发代码中异常处理更重要
4. **GIL影响**: CPU任务不要用线程，用进程
5. **I/O优先**: I/O操作优先用协程而不是线程
6. **性能测试**: 选择方案后要做实际性能测试

---

## 📖 参考资源

- Python threading 文档: https://docs.python.org/3/library/threading.html
- Python multiprocessing 文档: https://docs.python.org/3/library/multiprocessing.html
- Python asyncio 文档: https://docs.python.org/3/library/asyncio.html
- PEP 492 - Coroutines with async and await syntax
- GIL 详解: https://realpython.com/python-gil/

---

## 🎓 总结

| 方式 | 优点 | 缺点 | 最佳用途 |
|------|------|------|---------|
| **进程** | 真正并行，无GIL | 开销大，通信复杂 | CPU密集 |
| **线程** | 轻量，易用 | GIL限制，同步复杂 | I/O并发 |
| **协程** | 最轻，高效，简洁 | 不支持CPU密集 | 大量I/O |

**核心建议**: 优先考虑协程，其次线程，最后进程。但根据实际场景灵活选择！

