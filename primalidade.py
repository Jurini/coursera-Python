n = int(input('Digite um número e descubra sua primalidade: '))

if n % 2 != 0 and n % n == 0:
    print('primo')
else:
    print('não primo')
