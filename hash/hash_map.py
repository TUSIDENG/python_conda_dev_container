# 初始化哈希表
hmap: dict = {}

# 添加操作
# 在哈希表中添加键值对 (key, value)
hmap[12836] = "小哈"
hmap[15937] = "小啰"
hmap[16750] = "小算"
hmap[13276] = "小法"
hmap[10583] = "小鸭"

# 查询操作
# 向哈希表中输入键 key ，得到值 value
name: str = hmap[15937]
print(name)  # 输出：小啰

# 删除操作
# 在哈希表中删除键值对 (key, value)
hmap.pop(10583)
print(hmap)  # 输出：{12836: '小哈', 15937: '小啰', 16750: '小算', 13276: '小法'}

# 遍历哈希表
# 遍历哈希表中的所有键值对
for key, value in hmap.items():
    print(f"键: {key}, 值: {value}")

# 遍历键
for key in hmap.keys():
    print(f"键: {key}")

# 遍历值
for value in hmap.values():
    print(f"值: {value}")