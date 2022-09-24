
def files_clientes():
    try:
        file = open('clientes.txt', 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open('clientes.txt', 'wt+', encoding='utf-8')
            file.close()
        except:
            print('Erro de criação do arquivo - clientes')


def import_clientes():
    import pickle, os.path
    if os.path.getsize('clientes.txt') > 0:
        with open('clientes.txt', 'rb') as c:
            return pickle.load(c)
    else:
        return []
