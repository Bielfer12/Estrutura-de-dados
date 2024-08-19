class Quadrado:
    def __init__(self, tamanhodolado):
        self.tamanhodolado = tamanhodolado
    
    def mudarValorLado(self, novo_valor):
        self.tamanhodolado = novo_valor
            
    def RetornarValor(self):
        return self.tamanhodolado
    
    def calcArea(self):
        return self.tamanhodolado * self.tamanhodolado
        
tam1 = Quadrado(10)

print("Esse é valor atual do quadrado: ", tam1.RetornarValor())

tam1.mudarValorLado(20)
print("Novo valor do quadrado: ", tam1.RetornarValor())
print("Esta é a area do quadrado: ", tam1.calcArea())


            
        