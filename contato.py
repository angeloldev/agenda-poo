class Contato():
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome} - {self.telefone}'

#Fazer essa associação na main.py
#a = input("nome: ")
#b = input("telefone: ")
#c = Contato(a, b)
    