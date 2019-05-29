class MinhaClasse:
    #membro_cls pertence ao escopo da classe e nao a instancia
    membro_cls = 50
    def __init__(self):
        self.membro_inst = -10

    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)

i1 = MinhaClasse()
i2 = MinhaClasse()
print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

MinhaClasse.membro_cls = 1000

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)
