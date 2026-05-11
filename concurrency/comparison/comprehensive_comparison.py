"""
综合对比: 进程 vs 线程 vs 协程
全面对比三种并发方式的特点、优劣和适用场景
"""
import time
import threading
import multiprocessing
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ComparisonBenchmark:
    """并发方式对比基准测试"""
    
    @staticmethod
    def io_bound_task(duration=0.1):
        """I/O密集型任务"""
        time.sleep(duration)
        return f"完成I/O任务"
    
    @staticmethod
    async def async_io_task(duration=0.1):
        """异步I/O任务"""
        await asyncio.sleep(duration)
        return f"完成异步I/O任务"
    
    @staticmethod
    def cpu_bound_task(n=1000000):
        """CPU密集型任务"""
        return sum(i*i for i in range(n))

def print_section(title):
    """打印章节标题"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_comparison_table():
    """打印对比表格"""
    print_section("1. 特性对比表")
    
    table_data = [
        ("特性", "进程", "线程", "协程"),
        ("-" * 10, "-" * 15, "-" * 15, "-" * 15),
        ("创建开销", "很大", "中等", "很小"),
        ("内存占用", "很大(50MB+)", "中等(1-10MB)", "很小(<1KB)"),
        ("切换成本", "大(OS级)", "中等(OS级)", "小(用户态)"),
        ("最大数量", "数十到数百", "数百到数千", "数百万"),
        ("GIL影响", "无", "有", "无"),
        ("线程安全", "天然隔离", "需要同步机制", "单线程安全"),
        ("通信方式", "队列/管道", "共享内存+锁", "消息传递"),
        ("编程复杂度", "高", "中", "低"),
    ]
    
    for row in table_data:
        print(f"{row[0]:<12} | {row[1]:<15} | {row[2]:<15} | {row[3]:<15}")

def print_use_cases():
    """打印使用场景"""
    print_section("2. 适用场景对比")
    
    scenarios = {
        "进程 (Process)": [
            "✓ CPU密集型计算（数据处理、科学计算）",
            "✓ 需要利用多核CPU的场景",
            "✓ 需要进程隔离和容错",
            "✓ 执行外部程序或系统命令",
            "✗ 进程间通信复杂",
            "✗ 开销大，不适合轻量级任务",
        ],
        "线程 (Thread)": [
            "✓ I/O密集型任务（网络请求、文件操作）",
            "✓ 需要共享数据和通信",
            "✓ 简单的并发需求",
            "✓ 现有代码改造为并发",
            "✗ 受GIL限制，不适合CPU密集",
            "✗ 并发数量有限（通常<1000）",
            "✗ 需要处理线程同步和竞态条件",
        ],
        "协程 (Coroutine)": [
            "✓ 大量I/O并发操作",
            "✓ 高并发Web服务器",
            "✓ 网络爬虫和数据爬取",
            "✓ 需要处理数万个并发连接",
            "✓ 简洁的异步编程",
            "✗ 不支持CPU密集型计算",
            "✗ 学习曲线陡（async/await）",
        ],
    }
    
    for method, cases in scenarios.items():
        print(f"\n{method}:")
        for case in cases:
            print(f"  {case}")

def print_performance_guide():
    """打印性能指南"""
    print_section("3. 性能对比指南")
    
    scenarios = {
        "CPU密集型": {
            "排序": "多进程 > 串行 >> 多线程 ≈ 协程",
            "原因": "多进程利用多核，线程和协程受GIL限制",
            "建议": "使用多进程",
        },
        "I/O密集型": {
            "排序": "协程 > 多线程 ≥ 多进程 >> 串行",
            "原因": "协程切换成本最低，线程次之，进程开销太大",
            "建议": "优先协程，其次线程",
        },
        "内存占用": {
            "排序": "协程 << 线程 < 进程",
            "原因": "协程最轻量，线程中等，进程独立内存",
            "建议": "大并发优先协程，简单并发用线程",
        },
        "编程复杂度": {
            "排序": "协程 < 线程 < 进程",
            "原因": "协程顺序式，线程需要同步，进程通信复杂",
            "建议": "优先选择复杂度低的方案",
        },
    }
    
    for scenario, details in scenarios.items():
        print(f"\n{scenario}:")
        print(f"  性能排序: {details['排序']}")
        print(f"  原因: {details['原因']}")
        print(f"  建议: {details['建议']}")

def print_decision_tree():
    """打印决策树"""
    print_section("4. 选择决策树")
    
    decision_tree = """
    ┌─ 需要处理大量并发任务？
    │
    ├─ 是 ─────┐
    │          ├─ 是否为I/O密集型？
    │          │
    │          ├─ 是 ──→ 使用协程 ✓ (最优)
    │          │         理由: 成本最低，并发数可达百万
    │          │
    │          └─ 否 ──→ 是否为CPU密集型？
    │                    │
    │                    ├─ 是 ──→ 使用多进程 ✓
    │                    │         理由: 利用多核，避免GIL
    │                    │
    │                    └─ 否 ──→ 选择线程或协程
    │                              (根据复杂度)
    │
    └─ 否 ────────────────┐
                          ├─ 简单I/O任务？
                          │
                          ├─ 是 ──→ 使用线程 ✓
                          │         理由: 简单易用
                          │
                          └─ 否 ──→ 使用协程 ✓
                                    理由: 灵活高效
    """
    print(decision_tree)

def print_code_examples():
    """打印代码示例"""
    print_section("5. 代码示例对比")
    
    print("\n同一个I/O任务，三种方式的代码：")
    
    examples = {
        "串行执行": """
    def fetch_urls(urls):
        for url in urls:
            data = requests.get(url)  # 阻塞
            process(data)
        """,
        "多线程": """
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(fetch_and_process, urls)
        """,
        "多进程": """
    from multiprocessing import Pool
    
    with Pool(processes=4) as pool:
        pool.map(fetch_and_process, urls)
        """,
        "协程": """
    async def main():
        tasks = [fetch_and_process(url) for url in urls]
        await asyncio.gather(*tasks)
    
    asyncio.run(main())
        """,
    }
    
    for method, code in examples.items():
        print(f"\n{method}:")
        print(code)

def print_best_practices():
    """打印最佳实践"""
    print_section("6. 最佳实践")
    
    practices = [
        ("优先协程", "对于I/O密集型任务，协程是首选"),
        ("CPU用进程", "CPU密集任务必须用多进程，避免GIL"),
        ("简单用线程", "简单的I/O并发可以用线程（<1000个）"),
        ("避免过度", "并发度不是越高越好，根据实际需求"),
        ("监控资源", "定期检查内存和CPU占用"),
        ("测试性能", "不同场景选择后要做性能测试"),
        ("错误处理", "并发代码要特别注意异常处理"),
        ("资源释放", "确保线程/进程/协程正确完成和释放"),
    ]
    
    print("\n关键建议:")
    for i, (title, desc) in enumerate(practices, 1):
        print(f"  {i}. {title}")
        print(f"     → {desc}")

def print_summary():
    """打印总结"""
    print_section("7. 总结")
    
    summary = """
    | 方式   | 优点                      | 缺点                    | 最佳用途       |
    |--------|---------------------------|------------------------|-----------------|
    | 进程   | 真正并行, 无GIL限制       | 开销大, 通信复杂       | CPU密集任务    |
    | 线程   | 开销小, 易用              | GIL限制, 同步复杂      | 简单I/O并发    |
    | 协程   | 最轻量, 高并发, 易编写    | 不支持CPU密集, 学习曲线 | 大量I/O并发    |
    
    快速决策:
    • 处理大量并发I/O (>1000) → 协程
    • CPU密集计算            → 进程
    • 简单I/O并发 (<1000)    → 线程
    • 不确定就选择           → 协程 (现代Python标准)
    """
    print(summary)

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "进程 vs 线程 vs 协程 - 完全对比指南" + " " * 17 + "║")
    print("╚" + "=" * 68 + "╝")
    
    # 打印各个部分
    print_comparison_table()
    print_use_cases()
    print_performance_guide()
    print_decision_tree()
    print_code_examples()
    print_best_practices()
    print_summary()
    
    print("\n" + "=" * 70)
    print("  更多示例请查看各目录下的具体实现文件")
    print("=" * 70 + "\n")
