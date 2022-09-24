from detalhamentos import apresentacao, seguranca
from menu_inicial import tela_inicio



from fileslivros import import_livros
from filesclientes import import_clientes
from filescarrinho import import_carrinho
livrosbd = import_livros()
clientesbd = import_clientes()
carrinhobd = import_carrinho()



if __name__ == '__main__':
    apresentacao()
    seguranca()
    tela_inicio()
