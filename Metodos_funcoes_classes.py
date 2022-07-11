class Calculadora: #Classe
    def __init__(self, num1, num2): #Método
        self.valor_a = num1
        self.valor_b = num2

    def soma(self): #Instância
        return self.valor_a + self.valor_b

calculadora = Calculadora(10, 5)
print(calculadora.soma())
