# Definindo a classe agenda_telefonica para gerenciar os contatos.
class agenda_telefonica:
    # Inicializador da classe que cria uma lista vazia de contatos.
    def __init__(self):
        self.contacts = []  # Lista para armazenar os contatos

    # Método para adicionar um novo contato.
    def add_contact(self):
        # Solicita ao usuário que insira os dados do novo contato.
        name = input("Digite o nome: ")
        phone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        # Pergunta se o contato deve ser marcado como favorito.
        is_favorite = input("Marcar como favorito? (s/n): ").lower() == 's'

        # Cria um dicionário com os dados do contato e o adiciona à lista.
        contact = {
            "nome": name,
            "telefone": phone,
            "email": email,
            "favorito": is_favorite
        }
        self.contacts.append(contact)  # Adiciona o novo contato à lista
        print("\nContato adicionado com sucesso!\n")  # Mensagem de sucesso

    # Método para visualizar todos os contatos.
    def view_contacts(self):
        # Verifica se a lista de contatos está vazia.
        if not self.contacts:
            print("\nNenhum contato cadastrado.\n")
            return  # Retorna se não houver contatos.

        print("\nLista de contatos:\n")
        # Itera sobre a lista de contatos e imprime seus dados.
        for index, contact in enumerate(self.contacts):
            # Mostra os dados de cada contato, incluindo seu status de favorito.
            print(f"{index + 1}. {contact['nome']} - {contact['telefone']} - {contact['email']} - {'Favorito' if contact['favorito'] else 'Normal'}")

    # Método para editar um contato existente.
    def edit_contact(self):
        self.view_contacts()  # Exibe a lista de contatos
        try:
            # Solicita ao usuário o número do contato a ser editado.
            escolha = int(input("\nDigite o número do contato que deseja editar: ")) - 1
            # Verifica se a escolha é válida (dentro do intervalo de contatos).
            if escolha < 0 or escolha >= len(self.contacts):
                print("\nOpção inválida.\n")
                return

            # Recupera o contato selecionado e permite editar seus dados.
            contact = self.contacts[escolha]
            # Solicita ao usuário novos valores ou mantém os atuais se o campo for deixado em branco.
            contact['nome'] = input(f"Nome ({contact['nome']}): ") or contact['nome']
            contact['telefone'] = input(f"Telefone ({contact['telefone']}): ") or contact['telefone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            print("\nContato atualizado com sucesso!\n")
        except ValueError:
            print("\nEntrada inválida. Tente novamente.\n")  # Trata erro de entrada inválida.

    # Método para marcar/desmarcar um contato como favorito.
    def toggle_favorite(self):
        self.view_contacts()  # Exibe a lista de contatos
        try:
            # Solicita ao usuário o número do contato a ser marcado/desmarcado.
            escolha = int(input("\nDigite o número do contato para marcar/desmarcar como favorito: ")) - 1
            # Verifica se a escolha é válida.
            if escolha < 0 or escolha >= len(self.contacts):
                print("\nOpção inválida.\n")
                return

            # Altera o status de favorito do contato.
            self.contacts[escolha]['favorito'] = not self.contacts[escolha]['favorito']
            # Exibe o novo status do contato.
            status = "favorito" if self.contacts[escolha]['favorito'] else "normal"
            print(f"\nContato atualizado para {status}.\n")
        except ValueError:
            print("\nEntrada inválida. Tente novamente.\n")  # Trata erro de entrada inválida.

    # Método para exibir apenas os contatos favoritos.
    def view_favorites(self):
        # Filtra os contatos que estão marcados como favoritos.
        favorites = [c for c in self.contacts if c['favorito']]

        # Verifica se há contatos favoritos.
        if not favorites:
            print("\nNenhum contato marcado como favorito.\n")
            return

        print("\nLista de contatos favoritos:\n")
        # Exibe os contatos favoritos.
        for contact in favorites:
            print(f"{contact['nome']} - {contact['telefone']} - {contact['email']}")

    # Método para apagar um contato.
    def delete_contact(self):
        self.view_contacts()  # Exibe a lista de contatos
        try:
            # Solicita ao usuário o número do contato a ser apagado.
            escolha = int(input("\nDigite o número do contato que deseja apagar: ")) - 1
            # Verifica se a escolha é válida.
            if escolha < 0 or escolha >= len(self.contacts):
                print("\nOpção inválida.\n")
                return

            # Remove o contato da lista.
            self.contacts.pop(escolha)
            print("\nContato apagado com sucesso!\n")
        except ValueError:
            print("\nEntrada inválida. Tente novamente.\n")  # Trata erro de entrada inválida.

    # Método para exibir o menu e permitir interação com o usuário.
    def show_menu(self):
        while True:
            # Exibe as opções do menu.
            print("\nMenu:")
            print("1. Adicionar contato")
            print("2. Visualizar contatos")
            print("3. Editar contato")
            print("4. Marcar/Desmarcar favorito")
            print("5. Ver favoritos")
            print("6. Apagar contato")
            print("7. Sair")

            try:
                # Solicita ao usuário uma opção do menu.
                escolha = int(input("Escolha uma opção: "))

                # Verifica a escolha e chama o método correspondente.
                if escolha == 1:
                    self.add_contact()
                elif escolha == 2:
                    self.view_contacts()
                elif escolha == 3:
                    self.edit_contact()
                elif escolha == 4:
                    self.toggle_favorite()
                elif escolha == 5:
                    self.view_favorites()
                elif escolha == 6:
                    self.delete_contact()
                elif escolha == 7:
                    print("\nSaindo do aplicativo. Até logo!\n")
                    break  # Encerra o programa.
                else:
                    print("\nOpção inválida. Tente novamente.\n")
            except ValueError:
                print("\nEntrada inválida. Digite um número.\n")  # Trata erro de entrada inválida.

# Executa o programa quando o script é chamado diretamente.
if __name__ == "__main__":
    app = agenda_telefonica()  # Cria uma instância de agenda_telefonica
    app.show_menu()  # Exibe o menu para o usuário interagir
