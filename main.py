#if __name__ == '__main__':
#    n1 = float(input("Digite um número: "))
#    n2 = float(input("Digite o segundo número: "))
#    operador = input("Digite um operador: ")
#    if operador == "+":
#        print("Resultado = {}".format(n1 + n2))
#    elif operador == "-":
#        print("Resultado = {}".format(n1 - n2))
#    elif operador == "*":
#        print("Resultado = {}".format(n1 * n2))
#    elif operador == "/":
#        print("Resultado = {}".format(n1 / n2))
#    elif operador == "%":
#        print("Resultado = {}".format(n1 % n2))
#    else:
#        print("Operador inválido!")



def soma(n1, n2):
    print("Somando {} + {}".format(n1,n2))
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
    print("Subtraindo {} - {}".format(n1,n2))
    resultado = n1 - n2
    return resultado

def multiplicacao(n1, n2):
    print("Multiplicando {} * {}".format(n1,n2))
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    print("Dividindo {} / {}".format(n1,n2))
    if n2 == 0:
        print("Divisor não pode ser igual a zero.")
        resultado = "inválido"
        return resultado
    else:
        resultado = n1 / n2
        return resultado

def modulo(n1, n2):
    print("Módulo {} % {}".format(n1,n2))
    resultado = n1 % n2
    return resultado

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador: ")

if operador == "+":
    resultado = soma(n1,n2)
elif operador == "-":
    resultado = subtracao(n1,n2)
elif operador == "*":
    resultado = multiplicacao(n1,n2)
elif operador == "/":
    resultado = divisao(n1,n2)
elif operador == "%":
    resultado = modulo(n1,n2)
else:
    print("Operador inválido!")
    resultado = "inválido"

print("O resultado da operação é {}".format(resultado))










