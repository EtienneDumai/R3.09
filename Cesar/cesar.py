from collections import Counter
messageProf = "tuayyusskyjkymktyyosvrkykzzxgtwaorrkykztuaytgbutywaklgoxkjgbktzaxkyiktkyutzwakjkborgotkyinuykyjkyyuaxikyjkttaoykzjkjkygmxksktzykrrkybuayskzzktzktxkzgxjvuaxrkjotkxpktkbuoybxgosktzvgyrkvrgoyoxwakrutvkazezxuabkxhorhurknuhhozzurqokt"
message = "Hello, World!"
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

# algortihme d'euclide extendu : 
