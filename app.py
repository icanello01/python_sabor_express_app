import os

restaurantes = ["Sushi n' Roll", 'Pizza Place', 'Burger Joint']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')

    print('2. Listar restaurantes')

    print('3. Ativar/Desativar restaurante')

    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...\n')

def voltar_ao_menu_principal():
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{texto}\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante "{nome_do_restaurante}" cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados:\n')
    
    for restaurante in sorted(restaurantes):
        print(f'- {restaurante}')

    print()

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            print('Ativar/Desativar restaurante:')

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()