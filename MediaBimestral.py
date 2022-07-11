a = int(input('Entre com o primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Por favor, digite a nota: '))

b = int(input('Entre com o segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Por favor, digite a nota: '))

c = int(input('Entre com o terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Por favor, digite a nota: '))

d = int(input('Entre com o quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Por favor, digite a nota: '))

media = (a + b + c + d) / 4

if a <= 10 and b<= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))