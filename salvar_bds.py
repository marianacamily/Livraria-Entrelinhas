import pickle

def salvar_livros():
    from main import livrosbd
    file = open('livros.txt', 'wb')
    pickle.dump(livrosbd, file)
    file.close()


def salvar_clientes():
    from main import clientesbd
    file = open('clientes.txt', 'wb')
    pickle.dump(clientesbd, file)
    file.close()


def salvar_carrinho():
    from main import carrinhobd
    file = open('carrinho.txt', 'wb')
    pickle.dump(carrinhobd, file)
    file.close()
