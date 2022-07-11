n1 = 5
n2 = 10
n3 = 15
n4 = 20
n5 = 25

if n1 < n2 and n2 < n3 and n3 < n4 and n4 < n5:
    print('O menor valor é: {}'.format(n1))
elif n2 < n1 and n2 < n3 and n2 < n4 and n4 < n5:
    print('O menor valor é: {}'.format(n2))
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    print('O menor valor é: {}'.format(n3))
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    print('O menor valor é: {}'.format(n4))
else:
    print('O menor valor é: {}'.format(n5))
