class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome 
        self.salario = salario

    def mostraTela(self):
        return self.nome, self.salario
    
nome = input("Digite se nome: ")
sal = float(input("Digite seu salario: "))

func = Funcionario(nome,sal)

print(f"Funcionario: {func.mostraTela()}")