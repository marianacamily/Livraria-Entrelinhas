from funcoes_principais import cadastro_livro, pesquisa_livros, pesq_edicao


def tela_inicio():
    print('=' * 70)
    print('\033[0;35mMenu Inicial\033[m'.center(75))
    while True:
        print('Digite [\033[0;35m1\033[m] para Cadastrar Livros'.center(75))
        print('Digite [\033[0;35m2\033[m] para Pesquisar Livros'.center(75))
        print('Digite [\033[0;35m3\033[m] para Editar Livros'.center(75))
        print('Digite [\033[0;35m4\033[m] para Gerenciar Vendas'.center(75))
        print('Digite [\033[0;35m5\033[m] para ver Clientes Cadastrados'.center(75))
        print('Digite [\033[0;35m6\033[m] para ver Acervo de Livros'.center(75))
        print('Digite [\033[0;31m7\033[m] para \033[0;31mSair\033[m'.center(85))
        try:
            menu_dec = input(''.center(32))
        except:
            print('\033[0;31mValor Inválido\033[m - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] [\033[0;35m3\033[m] [\033[0;35m4\033[m] [\033[0;35m5\033[m] [\033[0;35m6\033[m] [\033[0;31m7\033[m]'.center(118))
        else:
            if menu_dec not in ['1', '2', '3', '4', '5', '6', '7']:
                print('\033[0;31mValor Inválido\033[m - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] [\033[0;35m3\033[m] [\033[0;35m4\033[m] [\033[0;35m5\033[m] [\033[0;35m6\033[m] [\033[0;31m7\033[m]'.center(118))
                continue
            else:
                break
    print('=' * 70)
    if menu_dec == '1':
        print('\033[0;35mCadastro de Livros\033[m'.center(78))
        cadastro_livro()
    elif menu_dec == '2':
        print('\033[0;35mPesquisa de Livros\033[m'.center(78))
        pesquisa_livros()
    elif menu_dec == '3':
        print('\033[0;35mEditar Livros\033[m'.center(78))
        pesq_edicao()
    elif menu_dec == '4':
        from main import carrinhobd
        print('\033[0;35mVendas Realizadas:\033[m'.center(78))
        print(carrinhobd)
        from funcoes_principais import voltar_menu
        voltar_menu()
    elif menu_dec == '5':
        from main import clientesbd
        print('\033[0;35mClientes Cadastrados:\033[m'.center(78))
        print(clientesbd)
        from funcoes_principais import voltar_menu
        voltar_menu()
    elif menu_dec == '6':
        from main import livrosbd
        print('\033[0;35mAcervo de Livros:\033[m'.center(78))
        print(livrosbd)
        from funcoes_principais import voltar_menu
        voltar_menu()
    elif menu_dec == '7':
        while True:
            print('\033[0;31mSair\033[m'.center(78))
            print('=' * 70)
            break






