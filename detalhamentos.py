
def apresentacao():
    print('=' * 70)
    print('\033[0;35mProjeto - Raciocínio Algorítmico\033[m'.center(70))
    print('Livraria \033[0;35mENTRE\033[mLINHAS - Bacharelado de Engenharia de Software'.center(70))
    print('1º Período'.center(70))
    print('Beatriz Petry Teixeira'.center(70))
    print('Mariana Camily dos Santos'.center(70))
    print('=' * 70)
    print(' ' * 15 + ' Sistema de Vendas - \033[0;35mENTRE\033[mLINHAS ' + ' ' * 22)
    print('=' * 70)
    while True:
        detalhamentos = input('Digite [\033[0;35mi\033[m] para ver informações básicas do projeto ou Clique [\033[0;35mENTER\033[m] para continuar: '.center(70))
        if detalhamentos == 'i':
            print('\033[0;35m1-\033[m Para fazer o Login estão disponíveis os seguintes usuários: Beatriz, Bia, Mariana, Mari e Maicris.'.center(70))
            print('\033[0;35m2-\033[m As senhas válidas (funcionam com todos os Logins) são: 123, 1234, 12345.'.center(70))
            print('\033[0;35m3-\033[m Caso esteja dando algum erro ao digitar o Preço de um livro, certifique-se que está utilizando pontos e não vírgulas.'.center(70))
            print('\033[0;35m4-\033[m Menção Honrosa: César - Sem ele nosso trabalho ia dar extremamente errado, sério.'.center(70))
            break
        elif detalhamentos == '':
            break
        else:
            print('\033[0;31mValor Inválido, Tente Novamente.\033[m'.center(70))
            continue

def seguranca():
    print('='*70)
    print('\033[0;35mENTRE\033[mLINHAS'.center(75))
    print('Acervo com cópias especiais de livros: \033[0;35mÁrea - Colecionadores\033[m'.center(75))
    while True:
        nome = input('Digite seu nome para fazer o Login no Sistema de Vendas:'.center(65))
        if nome not in ['Beatriz', 'Bia', 'Mariana', 'Mari', 'Maicris']:
            print('\033[0;31mDados de Login Inválidos, Tente Novamente.\033[m'.center(70))
            continue
        else:
            break
    print(f'Vendedor(a): {nome}'.center(65))
    while True:
        senha = input('Digite a Senha para verificação Obrigatória: '.center(65))
        if senha not in ['12345', '123', '1234']:
            print('\033[0;31mSenha Incorreta, Tente Novamente.\033[m'.center(70))
        else:
            break
