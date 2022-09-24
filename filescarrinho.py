
def files_carrinho():
    try:
        file = open('carrinho.txt', 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open('carrinho.txt', 'wt+', encoding='utf-8')
            file.close()
        except:
            print('Erro de criação do arquivo - clientes')


def import_carrinho():
    import pickle, os.path
    if os.path.getsize('carrinho.txt') > 0:
        with open('carrinho.txt', 'rb') as c:
            return pickle.load(c)
    else:
        return []

