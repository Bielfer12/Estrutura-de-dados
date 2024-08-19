class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if isinstance(alimento, Macaco):
            print(f"{self.nome} está comendo {alimento.nome}!")
            self.bucho.append(f"{alimento.nome} (macaco)")
            alimento.bucho = []
        else:
    
            print(f"{self.nome} está comendo {alimento}.")
            self.bucho.append(alimento)

    def verBucho(self):
        if not self.bucho:
            print(f"O estômago de {self.nome} está vazio.")
        else:
            print(f"O estômago de {self.nome} contém: {', '.join(self.bucho)}")

    def digerir(self):
        print(f"{self.nome} está digerindo o alimento.")
        self.bucho = [] 

def main():
    macaquinho1 = Macaco("Macaquinho1")
    macaquinho2 = Macaco("Macaquinho2")

    macaquinho1.comer("banana")
    macaquinho1.comer("maçã")
    macaquinho1.comer("laranja")

    macaquinho1.verBucho()

    macaquinho2.comer("pera")
    macaquinho2.comer("uva")

    macaquinho2.verBucho()

    macaquinho1.comer(macaquinho2)

    macaquinho1.verBucho()

    macaquinho2.verBucho()

    macaquinho1.digerir()
    macaquinho1.verBucho()

if __name__ == "__main__":
    main()
