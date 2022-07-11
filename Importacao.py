from Televisao import Televisao
from Contador_letras import contador_letras

if __name__ == '__main__':
    Televisao = Televisao()
    print(Televisao.ligada)
    Televisao.power()
    print(Televisao.ligada)
    Televisao.aumenta_canal()
    print(Televisao.canal)

    lista = ['gato']
    total_letras = contador_letras(lista)
    print(total_letras)