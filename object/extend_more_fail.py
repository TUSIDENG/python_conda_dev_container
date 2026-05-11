class X:
    pass

class Y:
    pass   


class A(X, Y):
    pass

class B(Y, X):
    pass

class D(A, B):
    pass   

D()
# TypeError: 无法创建实例 D，因为它有多个父类 A 和 B，
# 但它们之间没有明确的继承关系，导致无法确定调用哪个父类的 __init__ 方法。
print(D.__mro__)