import math

x1 = int(input('Digite o 1° dado: '))
y1 = int(input('Digite o 2° dado: '))
x2 = int(input('Digite o 3° dado: '))
y2 = int(input('Digite o 4° dado: '))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(d)
if d > 10:
    print('longe')
else:
    print('perto')

