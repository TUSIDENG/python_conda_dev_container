x = "hello"
y = "hello"
print(x is y)  # True，驻留了

x = "hello world"
y = "hello world"
print(x is y)  # False，含空格不驻留
