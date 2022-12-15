# Read/Write in file

import pathlib


if __name__ == '__main__':
    pathname = pathlib.Path(__file__).parent / 'data.txt'

    # with permet d'aliaser une instruction
    # f = open(pathname, 'r')
    # format pathlib.PosixPath
    # Mode d'ouverture de fichier
    #  Mode (r, a, r+, w...)

    with open(pathname, 'r') as f:
        data = f.read()
        print(data)
        f.close()


    print('\n')

    split = data.split(',')

    proper_split = []

    # Enumerate qui renvoie une clé et la valeur
    # C'est le format Array/List ( key => value)
    # A ne pas confondre Le format dictionnaire ( key : value)
    # Approche 1
    for key, value in enumerate(split):
        if key == 2:
            proper_split.append(value.split('. '))
        elif key == 3:
            proper_split.append(value.strip().split('. '))
        else:
            proper_split.append(value.strip().replace('.', ''))

    print(proper_split)

    print('\n')

    # Enumerate qui renvoie une clé et la valeur
    # C'est le format Array/List ( key => value)
    # A ne pas confondre Le format dictionnaire ( key : value)
    # Exercice:
    #  Trouver le moyen de remplacer les liste contenus dans dans 
    #  proper_split par leurs contenus afin d'obtenir une liste globales de séquence de phrase
    # Approche 2
    proper_split = []

    for key, value in enumerate(split):
        if (key == 2) or (key == 3) :
            proper_split.append(value.strip().split('. '))
        else:
            proper_split.append(value.strip().replace('.', ''))

    print(proper_split)