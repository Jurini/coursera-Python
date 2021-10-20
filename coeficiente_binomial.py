def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat


def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))


def testa_fatorial():
    if fatorial(1) == 1:
        print('✔️Funciona para 1')
    else:
        print('Não funciona para 1')
    if fatorial(2) == 2:
        print('✔️Funciona para 2')
    else:
        print('Não funciona para 2')
    if fatorial(0) == 1:
        print('✔️Funciona para 0')
    else:
        print('Não funciona para 0')
    if fatorial(5) == 120:
        print('✔️Funciona para 5')
    else:
        print('Não funciona para 5')


def testa_numero_binominal():
    if numero_binomial(2, 3) == 0:
        print('✔️Funciona, pois K não pode ser maior que N')
    else:
        print("O cálculo está incorreto")
    if numero_binomial(10, 20) == 0:
        print('✔️Funciona, pois K não pode ser maior que N')
    else:
        print("O cálculo está incorreto")
    if numero_binomial(5, 3) != 0:
        print('✔️Funciona')
    else:
        print("O cálculo está incorreto")


print(numero_binomial(6, 7))
testa_numero_binominal()
