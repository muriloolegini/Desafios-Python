conjunto = {1, 2, 3, 4}
conjunto2 = {4, 5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Deferença1: {}'.format(conjunto_diferenca1))
print('Diferença2: {}'.format(conjunto_diferenca2))

# conjunto.add(8)
# conjunto.discard(4)
#print(conjunto)