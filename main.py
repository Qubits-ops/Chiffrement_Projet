liste_lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
liste_cara_speciaux = ["é","!","à","à","â","ä","è","é","ê","ë","î","ï","ò","ô","ö","ù","û","ü","ç","?"]
#chiff_copier = []

while True:
    print("--------Bienvenue dans la matrix--------")
    print("Que souhaitez-vous faire ? Tapez le chiffre correspondant")
    print("-1- Chiffrer")
    print("-2- Déchiffrer")
    print("-3- Retour")
    choix = int(input("Entrez votre choix: "))
    if choix == 1:
        print("-1- Cesar chiffrement")
        print("-2- Xor chiffrement")
        choixchiff = int(input("Entrez votre choix: "))
        if choixchiff == 1:
            print("on va chiffrer avec notre ami cesar")
            def cara_erreur(lettre,liste_cara_speciaux):
                for i in range(len(liste_cara_speciaux)):
                    if liste_cara_speciaux[i] == lettre:
                        print("Pas de cara speciaux")
                        return True
            def chiffrage_cesar(lettre,liste_lettre,decal):
                for i in range(len(liste_lettre)):
                    if lettre == ' ':
                        return ' '
                    elif liste_lettre[i] == lettre:
                        return str(liste_lettre[i+decal])
            message_chiffre = str()
            while True:
                message_a_chiff = input("Entrez le message a chiffrer: ")
                for lettre2 in message_a_chiff:
                    cara_erreur(lettre2,liste_cara_speciaux)
                while True:
                    decal = int(input("Entrez le decalage que vous voulez: "))
                    print("Chiffre de décalage confirmé : " + str(decal))
                    break
                for lettre in message_a_chiff:
                    message_chiffre += chiffrage_cesar(lettre,liste_lettre,decal)
                print(message_chiffre)
                """chiff_copier.append(message_chiffre)
                cop =' '.join(chiff_copier)
                if cop == message_chiffre:
                print("deja chiffrer")
                break"""
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
        elif choixchiff == 2:
            print("on va chiffrer en xor")
            def xorCrypt(str, key):
                output = ""
                for x in range(0, len(str)):
                    output += chr(key ^ ord(str[x]))
                return output
            while True:
                message_a_chiff = input("Entrez le message a chiffrer: ")
                while True:
                    try:
                        clef = int(input("Entrez la cle de chiff que vous voulez: "))
                        break
                    except ValueError:
                        print("Mettez un chiffre !")
                print("Cle confirmé : " + str(clef))
                print(xorCrypt(message_a_chiff,clef))
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")

    elif choix == 2:
        print("on va dechiffrer")
    else:
        print("retour")
        break
        
    
