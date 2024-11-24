from collections import Counter
import string

# Alphabet de référence
alpha = string.ascii_lowercase

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

def pgcdEtendu(a, b):
    """
    Calcule le pgcd de deux nombres et l'inverse modulaire de 'a' modulo 'b' en utilisant l'algorithme d'Euclide étendu.
    
    Args:
    a (int): Le premier nombre.
    b (int): Le deuxième nombre.

    Returns:
    tuple: Un tuple (pgcd, x, y) où pgcd est le plus grand commun diviseur et (x, y) sont les coefficients de l'algorithme d'Euclide étendu.
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = pgcdEtendu(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverse(a, m):
    """
    Calcule l'inverse modulaire de 'a' modulo 'm'.
    
    Args:
    a (int): Le nombre dont on veut calculer l'inverse.
    m (int): Le module pour l'inverse.

    Returns:
    int: L'inverse de 'a' modulo 'm'.

    Raises:
    ValueError: Si l'inverse n'existe pas (c'est-à-dire si a et m ne sont pas premiers entre eux).
    """
    pgcd, x, _ = pgcdEtendu(a, m)
    if pgcd != 1:
        raise ValueError(f"Aucun inverse modulaire pour {a} modulo {m}")
    return x % m

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
    
    Args:
    message (str): Le message à analyser.

    Returns:
    list: Une liste des lettres du message, triée par fréquence décroissante.
    """
    c = Counter(char for char in message if char in alpha)
    freq = c.most_common()
    return [couple[0] for couple in freq]

def dechiffrer_avec_hypotheses(crypto):
    """
    Tente de déchiffrer un message crypté en utilisant des hypothèses sur les lettres les plus fréquentes.
    
    Args:
    crypto (str): Le message chiffré à déchiffrer.

    Returns:
    None: Affiche les hypothèses et les messages déchiffrés possibles.
    """
    # Identifier la lettre la plus fréquente dans le message crypté
    freqMess = analyse_frequence(crypto)
    lettre_codee_1 = freqMess[0]  # Lettre la plus fréquente
    code_lettre_codee_1 = code(lettre_codee_1)

    # Liste des hypothèses pour la deuxième lettre fréquente
    lettres_frequentes_en_clair = ['a', 't', 'o', 'i', 'n']
    messages_possibles = []

    for lettre_claire2 in lettres_frequentes_en_clair:
        try:
            # Indices pour 'e' (première lettre fréquente) et la lettre testée
            diff = (code(lettre_claire2) - code('e')) % 26

            # Calculer le delta entre la 2e lettre cryptée et la 1re
            for lettre_codee_2 in freqMess[1:]:  # Tester les autres lettres fréquentes du texte crypté
                code_lettre_codee_2 = code(lettre_codee_2)
                delta = (code_lettre_codee_2 - code_lettre_codee_1) % 26

                # Résoudre pour a et b
                a = (delta * inverse(diff, 26)) % 26
                b = (code_lettre_codee_1 - a * code('e')) % 26

                print(f"Essai avec : 'e' -> {lettre_codee_1}, {lettre_claire2} -> {lettre_codee_2}")
                print(f"Clés trouvées : a = {a}, b = {b}")

                # Déchiffrer le message
                message_dechiffre = dechiffre(crypto, a, b)
                messages_possibles.append((lettre_claire2, lettre_codee_2, message_dechiffre))
        except ValueError as e:
            print(f"Erreur pour {lettre_claire2} : {e}")

    # Afficher les résultats
    for lettre_claire2, lettre_codee_2, message in messages_possibles:
        print(f"Supposition : 'e' -> {lettre_codee_1}, {lettre_claire2} -> {lettre_codee_2}")
        print(f"Message déchiffré :\n{message}\n")

# Exemple d'appel de la fonction
c = "edqdkilofppxtdxndbmvbjaxqudkgxbwdkgudlyfblixpfbqudlwjljfkkxjqdlxndbmvbjifkkdqxjdkgwjdxbkqdwdpjtbduidndqwxkgdl"
crypto_message = 'atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx'
message_dechiffre = dechiffrer_avec_hypotheses(crypto_message)
