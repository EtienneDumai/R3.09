from collections import Counter
import string

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


def inverse(a, m):
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

def dechiffrer_avec_hypotheses(crypto):
    """
    Tente de déchiffrer un message crypté en utilisant des hypothèses sur les lettres les plus fréquentes.
    """
    # Connaitre la lettre qui apparait le plus dans le message codé (lettre la plus frequente)
    freq = analyse_frequence(crypto)
    lettrecode1 = freq[0]  # Lettre la plus fréquente
    codelettrecode1 = code(lettrecode1)

    # Liste des hypothèses pour la deuxième lettre fréquente
    lettres_frequentes_en_clair = ['a', 't', 'o', 'i', 'n']
    messages_possibles = []

    for lettre_claire2 in lettres_frequentes_en_clair:
        try:
            # Indices pour 'e' (première lettre fréquente) et la lettre testée
            diff = (code(lettre_claire2) - code('e')) % 26

            # Calculer le delta entre la 2e lettre cryptée et la 1re
            for lettrecodee2 in freq[1:]:  # Tester les autres lettres fréquentes du texte crypté
                code_lettre_codee_2 = code(lettre_codee_2)
                delta = (code_lettre_codee_2 - codelettrecode1) % 26

                # Résoudre pour a et b
                a = (delta * inverse(diff, 26)) % 26
                b = (codelettrecode1 - a * code('e')) % 26

                print(f"Essai avec : 'e' -> {lettrecode1}, {lettre_claire2} -> {lettre_codee_2}")
                print(f"Clés trouvées : a = {a}, b = {b}")

                # Déchiffrer le message
                message_dechiffre = dechiffre(crypto, a, b)
                messages_possibles.append((lettre_claire2, lettre_codee_2, message_dechiffre))
        except ValueError as e:
            print(f"Cela ne marche pas pour {lettre_claire2} : {e}")

    # Afficher les résultats
    for lettre_claire2, lettre_codee_2, message in messages_possibles:
        print(f"Supposition : 'e' -> {lettrecode1}, {lettre_claire2} -> {lettre_codee_2}")
        print(f"Message déchiffré :\n{message}\n")

# Exemple d'appel de la fonction
c = "edqdkilofppxtdxndbmvbjaxqudkgxbwdkgudlyfblixpfbqudlwjljfkkxjqdlxndbmvbjifkkdqxjdkgwjdxbkqdwdpjtbduidndqwxkgdl"
crypto_message = 'atgtqcxshzzdbtdltfepfjydgitqodfwtqoitxkhfxcdzhfgitxwjxjhqqdjgtxdltfepfjchqqtgdjtqowjtdfqgtwtzjbftictltgwdqotx'
message_dechiffre = dechiffrer_avec_hypotheses(crypto_message)
