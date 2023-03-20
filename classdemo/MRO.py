class A:
    var = 'A'


class B:
    var = 'B'


class C:
    var = 'C'


class D(A, B, C):

    def __init__(self):
        print(self.var)

obj = D()
