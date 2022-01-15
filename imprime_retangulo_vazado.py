coluna = int(input('digite a largura: '))
linha= int(input('digite a altura: '))

aux = coluna

while linha != 0:
    while coluna != 0:
        print('#', end='\t')
        coluna = coluna - 1
    linha = linha - 1
    print()
    coluna = aux



