class A:
    def __init__(self):
        self._var = 0

    @property
    def var(self):
        print("valor esta sendo lido")
        return self._var

    @var.setter
    def var(self, x):
        print("valor esta sendo escrito")
        self._var = x

a = A()
a.var = 15
print(a.var)