class Retangulo:
    def __init__(self, largura, altura):
        self.a = altura
        self.l = largura

    def area(self):
        return self.a * self.l

r1 = Retangulo(3,5)

print(r1.area())

