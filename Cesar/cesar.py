from collections import Counter
messageProf = "tuayyusskyjkymktyyosvrkykzzxgtwaorrkykztuaytgbutywaklgoxkjgbktzaxkyiktkyutzwakjkborgotkyinuykyjkyyuaxikyjkttaoykzjkjkygmxksktzykrrkybuayskzzktzktxkzgxjvuaxrkjotkxpktkbuoybxgosktzvgyrkvrgoyoxwakrutvkazezxuabkxhorhurknuhhozzurqokt"
message = "Hello, World!"
alpha = "abcdefghijklmnopqrstuvwxyz"
crypto2 = 'itxygjoqtchjoadzdjxhutjxxdqltfqtygtfwtctbthztogjtxfkkjoditzhqogtgldgxjwhfxidlghvtmxfgydghitwhfxtotxfqxhowhfxogdsjxxtmitxygjodidjq'
def code (lettre):
    code = 0
    if len (lettre) != 1:
        return -1
    else:
        for i in range (0, len (alpha)):
            if lettre == alpha[i]:
                code = i
    return code
print(code("z"))

def lettre(code):
    lettre = ""
    if code < 0 or code > 25:
        return -1
    else:
        lettre = alpha[code]
    return lettre

print(lettre(25))

def chiffreCesar(message, cle):
    cryptogramme = ""
    for i in message:
        cryptogramme += lettre((code(i) + cle) % 26)
    return cryptogramme
print(chiffreCesar(message, 3))

def dechiffreCesar(cryptogramme, cle):
    message = ""
    for i in cryptogramme:
        message += lettre((code(i) - cle) % 26)
    return message
c=Counter(messageProf)
freq=c.most_common(10)
print(freq)
print(dechiffreCesar(messageProf, (code("k")-code("e"))))

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

# Exemple d'utilisation
message = "election"
a = 3
b = 5
print(chiffreAffine(message, a, b))

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
#Exemple d'utilisation
cryptogramme = "rmrlkdvs"
c=Counter(crypto2)
freq=c.most_common(10)
print(freq)
a = 17
b = 3
print(dechiffreAffine(crypto2, a, b))
print(code('t'))
print(code('e'))
print(code('x'))
print(code('s'))