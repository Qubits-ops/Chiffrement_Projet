def cryptage(cle, lettre):
    """Encode une lettre grâce à une clé. L'encodage est le déplacement
    de la lettre dans l'alphabet par rapport à la valeur de la clé"""
    
    #Si la lettre est en majuscule
    if 65 <= ord(lettre) <= 90:
        return chr(65 + (ord(lettre)-65+cle) % 26)

    #Si la lettre est en minuscule
    elif 97 <= ord(lettre) <= 122:
        return chr(97 + (ord(lettre)-97+cle) % 26)
        
    #Si ce n'est pas une lettre
    else:
        return lettre
def RsaChiff(message, e, n):
    i = 0
    message_chiffre = ""
    while i != len(message):
        bloc = str(pow(ord(message[i]),e)%n)
        print(bloc)
        while(len(bloc) != 6):
            bloc = "0" + bloc
        message_chiffre += bloc
        i+=1
    return message_chiffre
def CesarChiff(message_a_chiff, decal):
    mot_crypte = ""
    for lettre in message_a_chiff:
        mot_crypte += cryptage(decal, lettre)

    return mot_crypte
def XorChiff(str, key):
    output = ""
    for x in range(0, len(str)):
        output += chr(key ^ ord(str[x]))
    return output
