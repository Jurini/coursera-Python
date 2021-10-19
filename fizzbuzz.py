x = int(input('Digite um número inteiro e descubra se ele é divisível por 3 e 5: '))

if x % 5 == 0 and x % 3 == 0 and x > 0:
    print('FizzBuzz')
else:
    print(x)
