a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print('Foi digitado número par!')
else:
    print('Foi digitado número ímpar!')