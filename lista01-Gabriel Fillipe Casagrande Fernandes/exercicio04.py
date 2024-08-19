class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5
        print(f"{self.nome} envelheceu. Idade: {self.idade} anos, Altura: {self.altura:.2f} cm")

    def engordar(self, peso):
        self.peso += peso
        print(f"{self.nome} engordou. Peso: {self.peso:.2f} kg")

    def emagrecer(self, peso):
        if self.peso - peso >= 0:
            self.peso -= peso
        else:
            self.peso = 0
        print(f"{self.nome} emagreceu. Peso: {self.peso:.2f} kg")

    def crescer(self, altura):
        self.altura += altura
        print(f"{self.nome} cresceu. Altura: {self.altura:.2f} cm")

def main():
    pessoa = Pessoa(nome="João", idade=20, peso=70.0, altura=175.0)

    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso:.2f} kg, Altura: {pessoa.altura:.2f} cm")
    
    pessoa.envelhecer()
    pessoa.envelhecer()
    
    pessoa.engordar(5.0)
    
    pessoa.emagrecer(2.0)

    pessoa.crescer(3.0)

    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso:.2f} kg, Altura: {pessoa.altura:.2f} cm")

if __name__ == "__main__":
    main()
