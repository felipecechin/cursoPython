class Retangulo:
    def __init__(self, largura, altura):
        self._altura = 0
        self._largura = 0
        #usa o set
        self.largura = largura
        self.altura = altura

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, num):
        if (not(isinstance(num, int) and num>0)):
            raise ValueError("Altura inválida: {}".format(num))
        self._altura = num

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, num):
        if (not(isinstance(num, int) and num>0)):
            raise ValueError("Largura inválida: {}".format(num))
        self._largura = num

    @property
    def area(self):
        return self._altura * self._largura

    # altura = property(fget=_get_altura, fset=_set_altura)
    # largura = property(fget=_get_largura, fset=_set_largura)
    # area = property(fget=_get_area)

r1 = Retangulo(largura=3, altura=5)
r1.largura = 10
r1.altura = 15
print(r1.altura)
print(r1.largura)
print(r1.area)
