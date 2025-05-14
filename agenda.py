from contato import Contato

class Agenda():
    def __init__(self):
        self.contatos = []
    
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(f'Contato encontrado: {contato}')
            else:
                print(f'Contato não encontrado')

    def adicionar_contato(self, nome, numero):
        contato = Contato(nome, numero)
        self.contatos.append(contato)
        print(f'Contato {nome} adicionado com sucesso!')

    def excluir_contato(self, nome):
        for contato in range(self.contato):
            if contato.nome == contato:
                del contato
                print(f'{contato} removido.')
                return
        print(f'{contato} não encontrado.')

    def listar_contatos(self):
        if not self.contatos:
            print(f'Sua lista de contatos está vazia!')
        else:
            print("\n Lista de contatos:")
            for contato in self.contatos:
                print(contato)
    
    def executar(self):
        while True:
            print("=================================================\n")
            print("Agenda Pessoal\n")
            print("\n")
            print("1 - Buscar contato\n")
            print("2 - Listar contatos\n")
            print("3 - Adicionar contato\n")
            print("4 - Excluir contato\n")
            print("5 - Sair da agenda\n")
            print("=================================================\n")
            comando = input(f'')

            if comando == "1":
                a = input(f"Digite o nome ou número do contato: ")
                self.buscar_contato(a)

            elif comando == "2":
                self.listar_contatos()

            elif comando == "3":
                nome = input(f'Digite o nome do contato: ')
                telefone = input(f'Digite o numero do contato: ')
                self.adicionar_contato(nome, telefone)

            elif comando == "4":
                nome = input("Nome do contato a excluir: ")
                self.excluir_contato(nome)

            elif comando == "5":
                break