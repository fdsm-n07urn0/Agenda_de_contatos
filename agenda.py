AGENDA = {}


def mostrar_contatos():
    if AGENDA:                          # Verifica se existe contato na agenda
        for contato in AGENDA:          # Faz mostra todos contatos (Um contato em cada linha)
            buscar_contato(contato)     
    else:
        print('>>>> Agenda vazia <<<<')


def buscar_contato(contato):                 # Chama essa função no for da função de cima pra mostra todos contatos
    try:
        print('Nome:', contato)                                # Mostra um contado
        print('Telefone:', AGENDA[contato]['telefone'])        # Filtra pela informação desejada
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print("-----------------------------")
    except KeyError:                           
        print('>>>> Contato inexistente <<<<')     
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)

def ler_detalhes_contatos():
    telefone = input('Telefone: ')
    email = input('Email: ')
    endereco = input('Endereço: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):        # Passar as informações que devem ser adicionadas
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print(f'>>>> Contato {contato} ADICIONADO / EDITADO com SUCESSO <<<<')
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f'>>>> Contato {contato} EXCLUIDO com SUCESSO <<<<')
        print()
    except KeyError:
        print('>>>> Contato inexistente <<<<')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:             # Reescrevi o arquivo sempre que é exportado
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))
        print('>>>> Agenda exportada com sucessso <<<<')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos <<<<')
        print(error)


def importar_contatos(nome_do_arquivo):               # Pega o nome do arquivo
    try:
        with open(nome_do_arquivo, 'r') as arquivo:   # Abre o arquivo passado pelo usuário em modo leitura
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')        
                
                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(contato, telefone, email, endereco)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado <<<<')
    except Exception as error:
        print('Algum erro inesperado ocorreu')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[contato] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>> Database carregado com sucesso')
        print('>>>> {} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado <<<<')
    except Exception as error:
        print('Algum erro inesperado ocorreu')
        print(error)


def imprimir_menu():
    print('''
        [1] Todos contatos
        [2] Buscar contato
        [3] Incluir contato
        [4] Editar contato
        [5] Excluir contato
        [6] Exportar contatos para CSV
        [7] Importar contatos CSV
        [0] Fechar agenda
        ''')
    print("-----------------------------")

# INICIO DO PROGRAMA
carregar()

while True:
    imprimir_menu()
    menu = input('Digite a opção desejada: ')

    if menu == '1':
        mostrar_contatos()

    elif menu == '2':
        contato = input('Nome do contato: ').capitalize()    
        buscar_contato(contato)

    elif menu == '3':
        contato = input('Nome do contato: ').capitalize()     
        try:
            AGENDA[contato]
            print('>>>> Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif menu == '4':
        contato = input('Nome do contato: ').capitalize()
        try:
            AGENDA[contato]
            print('>>>> Editando contato', contato)
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>>> Contato inexistente <<<<')

    elif menu == '5':
        contato = input('Nome do contato: ').capitalize()
        excluir_contato(contato)

    elif menu == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)

    elif menu == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)                  # Envia o nome do aquivo digitado para o importar_contatos()

    elif menu == '0':
        print('>>>> Fechando programa <<<<')
        break

    else:
        print('>>>> Opção invalida!!! <<<<')
