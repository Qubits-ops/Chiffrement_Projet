liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
liste_cara_speciaux = ["é","!","à","à","â","ä","è","é","ê","ë","î","ï","ò","ô","ö","ù","û","ü","ç","?"]

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
def CesarChiff(lettre,liste_lettre,decal):
    for i in range(len(liste_lettre)):
        if lettre == ' ':
            return ' '
        elif liste_lettre[i] == lettre:
            return str(liste_lettre[i+decal])
message_chiffre = str()
def XorChiff(str, key):
    output = ""
    for x in range(0, len(str)):
        output += chr(key ^ ord(str[x]))
    return output