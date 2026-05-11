a = [1, 2]
b = [3, 4]

a.append(b)
print(a)     # [1, 2, [3, 4]]

a = [1, 2]
a.extend(b)
print(a)     # [1, 2, 3, 4]

a.insert(1, 9)
print(a)     # [1, 9, 2, 3, 4]

a.insert(0,3)
print(a)     # [3, 1, 9, 2, 3, 4]

a.sort()
print(a)     # [1, 2, 3, 3, 4, 9]
