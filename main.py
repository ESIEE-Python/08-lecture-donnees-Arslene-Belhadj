#### Imports et définition des variables globales
"""Importation nécéssaire"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """

    l = []
    with open(filename, mode='r', encoding='utf8') as file:
        s = file.readlines()
        for line in s:
            l_prime = line.strip().split(';')
            l.append(list(map(int, l_prime)))

        # for nbLigne in range (0, s):
        #     for nbElement in range (s[0], s[len(s)]):
        #         l.append(s[nbElement])

    print (l)
    return l

def get_list_k(data, k):
    """ Méthode quiretourne la k-ème liste"""
    l = []
    l=data
    return l[k]

def get_first(l):
    """méthode qui retourne la première liste"""
    return l[0]

def get_last(l):
    """méthode qui retourne la dernière liste"""
    lenght = len(l)-1
    return l[lenght]

def get_max(l):
    """méthode qui retourne le maximum de cette liste"""
    return max(l)

def get_min(l):
    """méthode qui retourne le minimum de cette liste"""
    return min(l)

def get_sum(l):
    """méthode qui retourne la somme de cette liste"""
    somme = 0
    for i in l:
        somme += i
    return somme


#### Fonction principale


def main():
    """méthode main permettant le fonctionnement du code"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
