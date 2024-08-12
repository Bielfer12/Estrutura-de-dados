class Livros:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 

    def detalhe(self):
        print('Titulo (self.titulo)')
        print('Autor (self.autor)')
        print('Ano (self.ano)')

    def ler(self):
        print('Voce leu')

    def escrever(self):
        print('Voce escrever')

livro1 = Livros('Avatar','franl',2005)
livro1.detalhe()
livro1.ler()
livro1.escrever()