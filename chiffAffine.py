from collections import Counter
import string
crypto2 = 'atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx'


# Alphabet de référence
alpha = "abcdefghijklmnopqrstuvwxyz"

def code (lettre):
    code = 0
    if len (lettre) != 1:
        return -1
    else:
        for i in range (0, len (alpha)):
            if lettre == alpha[i]:
                code = i
    return code

def lettre(code):
    lettre = ""
    if code < 0 or code > 25:
        return -1
    else:
        lettre = alpha[code]
    return lettre


def inverse(n, m):
    """
    Calcule l'inverse modulaire de n modulo m en utilisant l'algorithme d'Euclide étendu.
    Retourne l'inverse si il existe, sinon retourne None si n et m ne sont pas premiers entre eux.
    """
    t, new_t = 0, 1
    r, new_r = m, n
    
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None  # n n'a pas d'inverse mod m
    if t < 0:
        t = t + m

    return t

def dechiffre(message_chiffre, a, b):
    """
    Déchiffre un message chiffré en utilisant le chiffrement affine.
    
    Args:
    message_chiffre (str): Le message chiffré à déchiffrer.
    a (int): La clé 'a' du chiffrement affine.
    b (int): La clé 'b' du chiffrement affine.

    Returns:
    str: Le message déchiffré.
    """
    invA = inverse(a, 26)  # Inverse modulaire de a modulo 26
    mess = ""
    for char in message_chiffre:
        if char in alpha:  # Ignorer les caractères non alphabétiques
            y = code(char)
            codeDecrypte = (invA * (y - b)) % 26
            mess += lettre(codeDecrypte)
        else:
            mess += char  # Garder les espaces et la ponctuation
    return mess

def analyse_frequence(message):
    """
    Analyse la fréquence des lettres dans un message et retourne les lettres les plus fréquentes.
    """
    c=Counter(message)
    freq=c.most_common(10)
    print(freq)

from collections import Counter

# Alphabet de référence
alpha = "abcdefghijklmnopqrstuvwxyz"

def analyse_frequence(message):
    """
    Effectue une analyse fréquentielle du message.
    :param message: Texte à analyser
    :param top_n: Nombre de lettres les plus fréquentes à extraire
    :return: Liste des lettres les plus fréquentes
    """
    c = Counter()
    for lettre in message:
        if lettre in alpha:
            c[lettre] += 1
    freq = c.most_common(5)
    return [lettre[0] for lettre in freq]  # Retourne seulement les lettres fréquentes

def dechiffreAffine(cryptogramme, a, b):
    """
    Déchiffre un cryptogramme chiffré avec le chiffrement affine.
    x = (a^(-1) * (y - b)) % 26
    """
    # Calculer l'inverse de a modulo 26
    a_inv = inverse(a, 26)
    if a_inv is None:
        return "La clé a n'a pas d'inverse modulo 26."

    message = ""
    for lettre in cryptogramme:
        if lettre.isalpha():
            # Convertir la lettre en minuscule et en code ASCII (a -> 0, b -> 1, ..., z -> 25)
            y = ord(lettre.lower()) - ord('a')
            # Appliquer la transformation affine inverse
            x = (a_inv * (y - b)) % 26
            # Convertir le résultat en lettre et ajouter au message
            message += chr(x + ord('a'))
        else:
            message += lettre
    return message

def affine_decrypt(message_chiffre):
    """
    Déchiffre un message chiffré en utilisant un encodage affine.
    Affiche exactement 5 messages déchiffrés maximum avec leurs clés.
    """
    modulus = 26

    # Lettres claires fréquentes limitées à ['a', 'i', 't', 's', 'n']
    lettres_claires = ['a', 'i', 't', 's', 'n']

    # Analyse fréquentielle du texte chiffré
    lettres_chiffrees = analyse_frequence(message_chiffre)
    lettrePluFreseq = lettres_chiffrees[0]
    lettre2PluFreseq = lettres_chiffrees[1]
        # On parcourt les lettres claires et chiffrées
    for iN in range(0,5):
        print(lettres_claires[iN])
        for lettre_chiffree in lettres_chiffrees:
            i_clair = code(lettres_claires[iN])
            
            # Calculer a en résolvant (a * i_clair) ≡ j_chiffre (mod 26)
            diff_i_j = (4 - i_clair) % modulus
            inverse_i_clair = inverse(i_clair, modulus)
            a = (inverse_i_clair * diff_i_j) % modulus
            # Calculer b
            b = ((code(lettrePluFreseq)-code(lettre2PluFreseq)) - a * i_clair) % modulus

            print(f"Clé a = {a}, Clé b = {b}\n")
            print("Message déchiffré :")
            print(dechiffreAffine(message_chiffre, a, b))



print(analyse_frequence(crypto2))
print(affine_decrypt(crypto2))
