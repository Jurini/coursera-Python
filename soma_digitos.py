n = int(input('Digite um número e descubra a sua soma: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
w = n // 10000 % 10
e = n // 100000 % 10
r = n // 1000000 % 10
t = n // 10000000 % 10
p = n // 100000000 % 10
i = n // 1000000000 % 10
o = n // 10000000000 % 10

soma = w + m + c + d + u + e + r + t + p + i + o

print(soma)
