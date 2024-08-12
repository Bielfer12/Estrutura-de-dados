class Carro:
    def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

    def exibir_infos(self):
                    print("Marca: (self.marca)")
                    print("Modelo: (self.modelo)")
                    print("Ano: (self.ano)")
                
    def acelerar(self):
                    print("O carro esta acelerando")

    def frear_carro(self):
                print("Esta freiando")


                carro1 = Carro("Toyota", "Corolla", 2022)
                carro1.exibir_infos()
                carro1.acelerar()
                carro1.frear_carro()