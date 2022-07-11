a = int(input('Entre com o primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Por favor, digite a nota: '))

b = int(input('Entre com o segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Por favor, digite a nota: '))

c = int(input('Entre com o terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Por favor, digite a nota: '))

d = int(input('Entre com o quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Por favor, digite a nota: '))

media = (a + b + c + d) / 4

if a <= 10 and b<= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
    if (media < 6):
        print('Reprovado')
    else:
        print('Parabens! Você passou')

# a = int(input('Informe um número? '))
# for num in range(a + 1):
#     div = 0
#
#     for x in range(1, num + 1):
#         resto = num % x
#         if (resto == 0):
#             div += 1
#
#     if div == 2:
#         print(num)

# a = int(input('Informe um número? '))
# div = 0
#
# for x in range(1, a + 1):
#     resto = a % x
#     if (resto == 0):
#         div += 1
#
# if div == 2:
#     print('O número {} é primo!'.format(a))
# else:
#     print('O número não {} é primo!'.format(a))