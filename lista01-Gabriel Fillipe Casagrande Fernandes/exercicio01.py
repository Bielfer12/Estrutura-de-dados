class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor


bola1 = Bola("Vermelho", 25.5, "Borrachas")
print("Cor inicial:", bola1.mostraCor())

bola1.trocaCor("Azul")
print("Nova cor:", bola1.mostraCor())
        
        