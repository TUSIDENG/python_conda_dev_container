class Pair:
    """键值对"""

    def __init__(self, key: int, val: str):
        """构造方法"""
        self.key = key
        self.val = val

class HashMapChaining:
    """链式地址哈希表"""

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        return key % self.capacity

    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """查询操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若找到 key ，则返回对应 val
        for pair in bucket:
            if pair.key == key:
                return pair.val
        # 若未找到 key ，则返回 None
        return None

    def put(self, key: int, val: str):
        """添加操作"""
        # 当负载因子超过阈值时，执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若遇到指定 key ，则更新对应 val 并返回
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        # 若无该 key ，则将键值对添加至尾部
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，从中删除键值对
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        """扩容哈希表"""
        # 暂存原哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        """打印哈希表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
            print(res)

if __name__ == "__main__":
    print("=" * 50)
    print("示例: 链式地址哈希表")
    print("=" * 50)

    hash_map = HashMapChaining()
    hash_map.put(1, "one")
    hash_map.put(2, "two")
    hash_map.put(6, "six")
    hash_map.put(3, "three")
    hash_map.put(4, "four")
    hash_map.put(5, "five")
    print("  添加键值对后:")
    hash_map.print()

    print("\n  查询 key=3:", hash_map.get(3))
    print("  查询 key=6:", hash_map.get(6))

    hash_map.put(3, "THREE")
    print("\n  更新 key=3 后:")
    hash_map.print()

    hash_map.remove(2)
    print("\n  删除 key=2 后:")
    hash_map.print()

    print("\n" + "=" * 50)
    print("演示: 单个bucket中存储多个元素")
    print("=" * 50)
    
    # 创建一个新的哈希表，容量较大以避免扩容
    bucket_demo = HashMapChaining()
    bucket_demo.capacity = 4
    bucket_demo.buckets = [[] for _ in range(bucket_demo.capacity)]
    bucket_demo.load_thres = 10.0  # 提高扩容阈值，防止扩容
    
    # 添加hash到同一个bucket的键值对
    # hash_func: key % 4
    # key=0,4,8,12都会hash到bucket[0]
    print("\n  添加hash到bucket[0]的多个键值对:")
    bucket_demo.put(0, "zero")    # 0 % 4 = 0
    bucket_demo.put(4, "four")    # 4 % 4 = 0
    bucket_demo.put(8, "eight")   # 8 % 4 = 0
    bucket_demo.put(12, "twelve") # 12 % 4 = 0

    bucket_demo.print()
    
    print("  bucket[0]中的元素:")
    print(f"    {bucket_demo.buckets[0]}")
    for pair in bucket_demo.buckets[0]:
        print(f"    key={pair.key}, val={pair.val}")
    
    print("\n  所有buckets的状态:")
    for i, bucket in enumerate(bucket_demo.buckets):
        print(f"    bucket[{i}]: ", end="")
        if bucket:
            pairs = [f"{pair.key}->{pair.val}" for pair in bucket]
            print(f"{pairs} (共{len(bucket)}个元素)")
        else:
            print("(空)")
    
    print("\n  通过链式地址法查询bucket[0]中的元素:")
    print(f"    get(0) = {bucket_demo.get(0)}")
    print(f"    get(4) = {bucket_demo.get(4)}")
    print(f"    get(8) = {bucket_demo.get(8)}")
    print(f"    get(12) = {bucket_demo.get(12)}")

    print("\n✓ 链式地址哈希表测试完成")