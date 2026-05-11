# read() 整个文件一次性吞进来
with open('./data.txt') as f:
    content = f.read()
    print(type(content))  # <class 'str'>
    print(repr(content))  # 'first line\nsecond line\nthird line\n'

# readline() 每次只读一行
with open('./data.txt') as f:
    line1 = f.readline()  # 'first line\n'
    print(line1)  # first line
    line2 = f.readline()  # 'second line\n'
    print(line2)  # second line
    line3 = f.readline()  # 'third line\n'
    print(line3)  # third line
    line4 = f.readline()  # ''  读完了返回空字符串
    print(line4)  # 空字符串

# readlines() 全部读进来，按行切成列表
with open('./data.txt') as f:
    lines = f.readlines()
    print(lines)  # ['first line\n', 'second line\n', 'third line\n']
