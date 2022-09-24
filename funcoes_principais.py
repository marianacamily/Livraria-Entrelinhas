
def cadastro_livro():
    global quant, preco
    from salvar_bds import salvar_livros
    from main import livrosbd
    while True:
        codigo = input('Codigo do livro: '.center(70))
        nom_aut = input('Nome e Autor do livro: '.center(70))
        while True:
            try:
                quant = int(input('Quantidade em estoque: '.center(70)))
            except:
                print('\033[0;31mValor Inválido\033[m'.center(80))
                continue
            else:
                break
        while True:
            try:
                preco = float(input('Valor: '.center(70)))
            except:
                print('\033[0;31mValor Inválido\033[m'.center(80))
                continue
            else:
                break
        livro = {'Código': codigo, 'Nome - Autor': nom_aut, 'Estoque': quant, 'Preço': preco}
        livrosbd.append(livro)
        print(livro)
        salvar_livros()
        print('Livro adicionado com \033[0;35mSucesso\033[m ao Banco de Dados!'.center(80))

        while True:
            try:
                livros_dec = str(input('Deseja Cadastrar mais livros? Digite [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(80)))
            except:
                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
            else:
                if livros_dec not in ['1', '2']:
                    print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    continue
                else:
                    break
        if livros_dec == '1':
            continue
        elif livros_dec == '2':
            voltar_menu()
            break
        break

def voltar_menu():
    while True:
        try:
            sair_dec = input('Deseja ir para o Menu Inicial? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(80))
        except:
            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
        else:
            if sair_dec not in ['1', '2']:
                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                continue
            else:
                break
    if sair_dec == '1':
        from menu_inicial import tela_inicio
        tela_inicio()
    elif sair_dec == '2':
        print('='*70)
        pass


def pesq_edicao():
    from main import livrosbd
    import collections
    from salvar_bds import salvar_livros
    while True:
        pesq = input("Código do Livro que deseja editar: ".center(70))
        find = False
        for data in livrosbd:
            if data['Código'] == pesq:
                find = True
                print("\033[0;35mLivro encontrado:\033[m".center(80))
                print(data)
                lista = []
                lista.append(data)
                livrosbd.remove(data)
                salvar_livros()
                quant = int(input('Digite o número de livros que chegaram no estoque: '))
                dicio2 = {'Estoque': quant}
                lista.append(dicio2)
                print(lista)
                Counter = collections.Counter()
                for d in lista:
                    Counter.update(d)
                resultado = dict(Counter)
                livrosbd.append(dict(Counter))
                salvar_livros()
                print(f'Seu estoque foi atualizado:,', str(resultado))
                voltar_menu()
                break
        if not find:
            print("\033[0;31mLivro não encontrado.\033[m".center(80))
            while True:
                while True:
                    try:
                        dec_n_enc = input('Você deseja pesquisar algum outro Livro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                    except:
                        print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    else:
                        if dec_n_enc not in ['1', '2']:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            continue
                        else:
                            break
                if dec_n_enc == '1':
                    pesq_edicao()
                    break
                elif dec_n_enc == '2':
                    voltar_menu()
                    break
        break


def pesquisa_livros():
    global cliente
    from main import livrosbd, carrinhobd
    from salvar_bds import salvar_carrinho
    while True:
        try:
            pesq_dec = input('Você deseja pesquisar [\033[0;35m1\033[m] por Código ou [\033[0;35m2\033[m] por Nome - Autor? '.center(75))
        except:
            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
        else:
             if pesq_dec not in ['1', '2']:
                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                continue
             else:
                break
    if pesq_dec == '1':
        pesq = input("Código do Livro que deseja pesquisar: ".center(70))
        find = False
        for data in livrosbd:
            if data['Código'] == pesq:
                find = True
                print("\033[0;35mLivro encontrado:\033[m".center(80))
                print(data)
                carrinho = ['Carrinho:']
                while True:
                    try:
                        carrinho_dec = input('Deseja adicionar esse livro ao carrinho? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                    except:
                        print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    else:
                        if carrinho_dec not in ['1', '2']:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            continue
                        else:
                            break
                if carrinho_dec == '1':
                    carrinho.append(data)
                    print('Livro adicionado com \033[0;35mSucesso:\033[m.'.center(80))
                    print(carrinho)
                    while True:
                        try:
                            dec_finalizar = input('Deseja finalizar sua compra? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                        except:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                        else:
                            if dec_finalizar not in ['1', '2']:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                continue
                            else:
                                break
                    if dec_finalizar == '1':
                        while True:
                            try:
                                dec_cadastro = input('Já possui Cadastro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                            except:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            else:
                                if dec_cadastro not in ['1', '2']:
                                    print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                    continue
                                else:
                                    break
                        if dec_cadastro == '1':
                            pesquisa_cliente()
                            carrinhobd.append(carrinho)
                            print(carrinho)
                            print('Compra Realizada com \033[0;35mSucesso.\033[m'.center(85))
                        elif dec_cadastro == '2':
                            cadastro_cliente()
                            carrinhobd.append(carrinho)
                            print(carrinho)
                            print('Compra Realizada com \033[0;35mSucesso.\033[m'.center(85))
                        salvar_carrinho()
                        voltar_menu()
                    else:
                        voltar_menu()
                elif carrinho_dec == '2':
                    while True:
                        try:
                            dec_n_enc = input('Você deseja pesquisar algum outro Livro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                        except:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                        else:
                            if dec_n_enc not in ['1', '2']:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                continue
                            else:
                                break
                    if dec_n_enc == '1':
                        pesquisa_livros()
                    elif dec_n_enc == '2':
                        voltar_menu()
                        break
        if not find:
            print("\033[0;31mLivro não encontrado.\033[m".center(80))
            while True:
                while True:
                    try:
                        dec_n_enc = input('Você deseja pesquisar algum outro Livro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                    except:
                        print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    else:
                        if dec_n_enc not in ['1', '2']:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            continue
                        else:
                            break
                if dec_n_enc == '1':
                    pesquisa_livros()
                else:
                    break
                break
    elif pesq_dec == '2':
        pesq = input("Nome - Autor do Livro que deseja pesquisar: ".center(70))
        find = False
        for data in livrosbd:
            if data['Nome - Autor'] == pesq:
                find = True
                print("\033[0;35mLivro encontrado:\033[m".center(80))
                print(data)
                carrinho = ['Carrinho:']
                while True:
                    try:
                        carrinho_dec = input('Deseja adicionar esse livro ao carrinho? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                    except:
                        print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    else:
                        if carrinho_dec not in ['1', '2']:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            continue
                        else:
                            break
                if carrinho_dec == '1':
                    carrinho.append(data)
                    print('Livro adicionado com \033[0;35mSucesso:\033[m.'.center(80))
                    print(carrinho)
                    while True:
                        try:
                            dec_finalizar = input('Deseja finalizar sua compra? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                        except:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                        else:
                            if dec_finalizar not in ['1', '2']:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                continue
                            else:
                                break
                    if dec_finalizar == '1':
                        while True:
                            try:
                                dec_cadastro = input('Já possui Cadastro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                            except:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            else:
                                if dec_cadastro not in ['1', '2']:
                                    print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                    continue
                                else:
                                    break
                        if dec_cadastro == '1':
                            pesquisa_cliente()
                            carrinhobd.append(carrinho)
                            print(carrinho)
                            print('Compra Realizada com \033[0;35mSucesso.\033[m'.center(85))
                        elif dec_cadastro == '2':
                            cadastro_cliente()
                            carrinhobd.append(carrinho)
                            print(carrinho)
                            print('Compra Realizada com \033[0;35mSucesso.\033[m'.center(85))
                        salvar_carrinho()
                        voltar_menu()
                    else:
                        voltar_menu()
                elif carrinho_dec == '2':
                    while True:
                        try:
                            dec_n_enc = input('Você deseja pesquisar algum outro Livro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                        except:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                        else:
                            if dec_n_enc not in ['1', '2']:
                                print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                                continue
                            else:
                                break
                    if dec_n_enc == '1':
                        pesquisa_livros()
                    else:
                        voltar_menu()
                        break
        if not find:
            print("\033[0;31mLivro não encontrado.\033[m".center(80))
            while True:
                while True:
                    try:
                        dec_n_enc = input('Você deseja pesquisar algum outro Livro? [\033[0;35m1\033[m] para Sim ou [\033[0;35m2\033[m] para Não: '.center(75))
                    except:
                        print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                    else:
                        if dec_n_enc not in ['1', '2']:
                            print('Valor Inválido - Opções: [\033[0;35m1\033[m] [\033[0;35m2\033[m] '.center(90))
                            continue
                        else:
                            break
                if dec_n_enc == '1':
                    pesquisa_livros()
                else:
                    break
                break



def cadastro_cliente():
    from salvar_bds import salvar_clientes
    from main import clientesbd
    cpf = input('CPF do cliente: '.center(70))
    nome_cliente = input('Nome do cliente: '.center(70))
    email = input('E-mail do cliente: '.center(70))
    telefone = input('Telefone do cliente: '.center(70))
    cliente = {'CPF': cpf, 'Nome': nome_cliente, 'Email': email, 'Telefone': telefone}
    clientesbd.append(cliente)
    print(cliente)
    salvar_clientes()
    print('Cliente adicionado com \033[0;35mSucesso\033[m ao Banco de Dados!'.center(80))

def pesquisa_cliente():
    from main import clientesbd
    pesq = input("Digite o CPF do cliente que deseja encontrar: ")
    find = False
    for data in clientesbd:
        if data['CPF'] == pesq:
            find = True
            print("Cliente encontrado:")
            print(data)
    if not find:
        print("Esse cliente não foi encontrado")
        cadastro_cliente()





