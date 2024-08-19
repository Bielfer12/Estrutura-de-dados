class Televisor:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def mudarCanal(self, novo_canal):
        self.canal = novo_canal
    
    def mostrarCanal(self):
        return self.canal
    
    def mostrarVolume(self):
        return self.volume

    def abaixarVolume(self, abaixar):
        if self.volume - abaixar < 0:
            self.volume = 0
            print("Ja esta em 0")
        else:
            self.volume -= abaixar
            return
    
    def aumentarVolume(self, aumentar):
        if self.volume + aumentar > 100:
            self.volume = 100
            print("Ja esta em 100")
        else:
            self.volume += aumentar
    
cal = float(input("Digite o canal: "))
vol = float(input("Digite o volume: "))

tv1 = Televisor(cal,vol) 

while True:
    print("1 - Mostrar Volume/canal")
    print("2 - Aumentar Volume")
    print("3 - Diminuir Volume")
    print("4 - Trocar Canal")
    print("5 - Sair")

    escolha = float(input("Número a ser escolhido: "))

    match escolha:
        case 1:
         print(f"Seu canal: {tv1.mostrarCanal()} \nSeu volume: {tv1.mostrarVolume()}")    
         break
        case 2:
            aumento = float(input("Quanto de volume irá aumentar: "))
            tv1.aumentarVolume(aumento)
            print(f"Seu volume foi para:{tv1.mostrarVolume()}")
            break
        case 3:
            abaixo = float(input("Quanto de volume irá abaixar: "))
            tv1.abaixarVolume(abaixo)
            print(f"Seu volume foi para:{tv1.mostrarVolume()}")
            break
        case 4:
            trocar = float(input("Qual canal quer ir: "))
            tv1.mudarCanal(trocar)
            print(f"Seu novo canala é: {tv1.mostrarCanal()}")
        case 5:
            break
        case _:
            print("Digitou numero errado")


