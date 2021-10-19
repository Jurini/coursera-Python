import math

# Nenhuma raiz real: quando delta for menor que zero. (negativo)
# Uma única raiz real: quando delta for igual a zero. (nulo)
# Duas raízes reais: quando delta for maior que zero. (positivo)

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

delta = b ** 2 - 4 * a * c


def bhaskara_(a, b, delta):
    return (-b - math.sqrt(delta)) / (2 * a)


def bhaskara(a, b, delta):
    return (-b + math.sqrt(delta)) / (2 * a)


if delta == 0:
    raiz1 = bhaskara()
    print('a raiz desta equação é', raiz1)
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raiz1 = bhaskara()
        raiz2 = bhaskara_()
        print('as raízes da equação são', raiz2, 'e', raiz1)
