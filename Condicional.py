a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
c = int(input('Entre com o terceiro valor: '))

if a > b and a > c:
    print('O maior valor é: {}'.format(a))
elif b > a and b > c:
    print('O maior valor é: {}'.format(b))
else:
    print('O maior valor é: {}'.format(c))
print('Fim')