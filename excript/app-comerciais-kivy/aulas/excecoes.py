try:
    a = 10/0
    print(a)
except ZeroDivisionError:
    print("Deu erro")


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError as e:
            print(e)
            print(e.args)
            print("Número inválido")

def erro(x):
    try:
        eval(x)
    except TypeError as e:
        print(e)
    else: #nao ocorre erro
        print("Nenhuma excecao ocorreu")
    finally:
        print("Sempre executa")




num1 = input_float("Digite um número:")
num2 = input_float("Digite outro número:")

print(num1/num2)

erro("int+int")