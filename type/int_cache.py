a = 256
b = 256
print(a is b)  # True，命中缓存

a = 1000000000
b = 1000000000
print(a is b)  # True，命中缓存


print(a is b)  # False，超出缓存范围，各自创建了新对象
