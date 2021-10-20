import math


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('a raiz desta equação é', raiz1)
    else:
        if d < 0:
            print('esta equação não possui raízes reais')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('as raízes da equação são', raiz2, 'e', raiz1)


main()
