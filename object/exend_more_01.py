class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")

class C(A):
    def do(self):
        print("C")

class D(B, C):
    pass

d = D()
d.do()  # 输出 B
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
