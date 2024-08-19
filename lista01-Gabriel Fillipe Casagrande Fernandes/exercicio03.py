class Retangulo:
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura
    
    def mudarValorLado(self, novo_base, novo_altura):
        self.base = novo_base
        self.altura = novo_altura
            
    def RetornarValorLado(self):
        return self.altura, self.base
            
    def calculoArea(self):
        return self.base * self.altura
            
    def calculoPerimetro(self):
        return  (self.base * 2) + (self.altura * 2)
        
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

retangulo1 = Retangulo(base = 4, altura = 4)

area = retangulo1.calculoArea()
perimetro = retangulo1.calculoPerimetro()

print(f"Valores do retângulo: Base = {retangulo1.base}, Altura = {retangulo1.altura}")
print(f"Cálculo da Área: {area}")
print(f"Cálculo do Perímetro: {perimetro}")

