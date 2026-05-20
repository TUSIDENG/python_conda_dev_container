lst = [1, 2, 3]
lst[0] = 99       # 没问题
lst.append(4)     # 没问题
print(lst)  # [99, 2, 3, 4]  完全合法

tpl = ([1, 2], [3, 4])
tpl[0][0] = 99    # 没问题，修改了列表的内容，但没有修改元组的结构
print(tpl)  # ([99, 2], [3, 4])  完全合法


tpl = (1, 2, 3)
tpl[0] = 99       # TypeError: 'tuple' object does not support item assignment


