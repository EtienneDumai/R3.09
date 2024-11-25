
messageProf = "tuayyusskyjkymktyyosvrkykzzxgtwaorrkykztuaytgbutywaklgoxkjgbktzaxkyiktkyutzwakjkborgotkyinuykyjkyyuaxikyjkttaoykzjkjkygmxksktzykrrkybuayskzzktzktxkzgxjvuaxrkjotkxpktkbuoybxgosktzvgyrkvrgoyoxwakrutvkazezxuabkxhorhurknuhhozzurqokt"
message = "Hello, World!"
alpha = "abcdefghijklmnopqrstuvwxyz"
lettre_alpha = {i: lettre for i, lettre in enumerate(alpha)}
crypto2 = 'atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx'
from collections import Counter 
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

#Inverse modulaire : 
def inverse_modulaire(n, m):
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

# Chiffrement affine :
def chiffreAffine(message, a, b):
    """
    Chiffre un message en utilisant le chiffrement affine.
    y = (a * x + b) % 26
    """
    cryptogramme = ""
    for lettre in message:
        if lettre.isalpha():
            # Convertir la lettre en minuscule et en code ASCII (a -> 0, b -> 1, ..., z -> 25)
            x = ord(lettre.lower()) - ord('a')
            # Appliquer la transformation affine
            y = (a * x + b) % 26
            # Convertir le résultat en lettre et ajouter au cryptogramme
            cryptogramme += chr(y + ord('a'))
        else:
            cryptogramme += lettre
    return cryptogramme



#dechiffrement affine :
def dechiffreAffine(cryptogramme, a, b):
    """
    Déchiffre un cryptogramme chiffré avec le chiffrement affine.
    x = (a^(-1) * (y - b)) % 26
    """
    # Calculer l'inverse de a modulo 26
    a_inv = inverse_modulaire(a, 26)
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
crypto2 = 'atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx'
def dechiffreAffine(message_crypte, a, b):
    """
    Déchiffre un message en utilisant la clé affine.
    Args:
    - message_crypte (str): le message crypté
    - a (int): coefficient multiplicatif de la clé affine
    - b (int): décalage de la clé affine

    Returns:
    - str: le message déchiffré
    """
    message_dechiffre = ""
    inverse_a = inverse_modulaire(a, 26)
    if inverse_a is None:
        raise ValueError(f"Pas d'inverse modulaire pour a = {a}")

    for lettre in message_crypte:
        if lettre in alpha:  # Vérifie que la lettre est dans l'alphabet
            code_lettre = code(lettre)
            code_lettre_claire = (inverse_a * (code_lettre - b)) % 26
            message_dechiffre += lettre_alpha[code_lettre_claire]
        else:
            message_dechiffre += lettre  # Conserve les caractères non-alphabétiques
    return message_dechiffre


def crypto22(message_crypte):
    """
    Déchiffre un message en utilisant une boucle pour tester 5 hypothèses de lettres fréquentes en clair.
    Calcule dynamiquement a et b à chaque hypothèse.

    Args:
    - message_crypte (str): le message crypté à déchiffrer.

    Returns:
    - None: Affiche les messages déchiffrés pour chaque hypothèse.
    """
    modulo = 26

    # Analyse fréquentielle du texte crypté
    c = Counter(message_crypte)
    freq = c.most_common(2)
    lettre_codee_1 = freq[0][0]
    lettre_codee_2 = freq[1][0]
    code_lettre_codee_1 = code(lettre_codee_1)
    code_lettre_codee_2 = code(lettre_codee_2)
    compteur=1
    print(f"Lettre codée 1 : '{lettre_codee_1}' (la plus frequente dans le texte fréquente)")
    print(f"Lettre codée 2 : '{lettre_codee_2}' (deuxième plus fréquente)\n")

    # Lettres fréquentes en clair (hypothèses)
    lettres_frequentes_en_clair = ['i', 'a', 's', 't', 'n']
    for lettre_claire in lettres_frequentes_en_clair:
        print(f"ESSAI {compteur}")
        print(f"Test de l'hypothèse : '{lettre_claire}' comme 2e lettre fréquente en clair")
        compteur+=1
        # Calcul des différences pour trouver a
        delta_code = (code_lettre_codee_2 - code_lettre_codee_1) % modulo
        diff_clair = (code(lettre_claire) - code('e')) % modulo
        inverse_diff_clair = inverse_modulaire(diff_clair, modulo)

        if inverse_diff_clair is None:
            print(f"Pas d'inverse modulaire pour la différence {diff_clair}. Hypothèse ignorée.\n")
            continue

        # Calcul de a et b
        a = (delta_code * inverse_diff_clair) % modulo
        b = (code_lettre_codee_1 - a * code('e')) % modulo

        # Vérification des clés
        if inverse_modulaire(a, modulo) is None:
            print(f"Clé invalide : a = {a}, b = {b}. Hypothèse ignorée.\n")
            continue

        # Déchiffrement du message
        message_dechiffre = dechiffreAffine(message_crypte, a, b)
        if message_dechiffre is None:
            print(f"Impossible de déchiffrer avec a = {a}, b = {b}\n")
            continue

        print(f"Clés trouvées : a = {a}, b = {b}")
        print(f"Message déchiffré :\n{message_dechiffre}\n")


# Exemple d'appel
crypto2 = "atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx"
crypto22(crypto2)

    