def minha_func():
    print("Opa")

def soma(x,y):
    total = x+y
    return total

def login(usuario="root", senha="123"):
    print("Usuario", usuario)
    print("Senha", senha)


minha_func()
resultado = soma(2,4)
print("resultado ",resultado)
#parametros nomeados
login(senha="opa", usuario="login")

def func():
    return 20,30

x, y = func()
print("x", x, "y", y)


def lista_de_argumentos(*lista):
    print(lista)

lista_de_argumentos(1,2,3,4,5,6)

def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)

lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)


def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)


tupla = "felipe", "cechin", 25
pessoa(*tupla)

d = {"nome":"felipe","sobrenome":"cechin","idade":20}
pessoa(**d)




def function(a,b,c):
    print(a)
    print(b)
    print(c)

tupla = 1, 2, 25
lista = [*tupla]
lista.sort()
function(*lista)

def func():
    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local +=1
        print(var_local)

    func_interna()

func()



