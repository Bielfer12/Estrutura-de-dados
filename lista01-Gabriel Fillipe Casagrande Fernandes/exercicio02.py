class Quadrado:
    def __init__(self, tamanhodolado = 10):
        self.tamanhodolado = tamanhodolado
    
    def mudarValorLado(self, novo_valor):
        self.tamanhodolado = novo_valor
            
    def RetornarValor(self):
        return self.tamanhodolado
        
tam1 = float(input("Digite o novo valor do quadrado: "))
tam2 = Quadrado(tam1)
print("Novo valor do quadrado: ", tam2.RetornarValor())
# PERGUNTAR ALGO

            
        