
def files_livros():
    try:
        file = open('livros.txt', 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open('livros.txt', 'wt+', encoding='utf-8')
            file.close()
        except:
            print('Erro de criação do arquivo - livros')


def import_livros():
    import pickle, os.path
    if os.path.getsize('livros.txt') > 0:
        with open('livros.txt', 'rb') as b:
            return pickle.load(b)
    else:
        return []

