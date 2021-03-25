from chiff import *
from math2 import *
from time import *
import os
liste1 = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
path = "/Users/Tarkov/Desktop/general"
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
        print("-3- Rsa chiffrement")
        choixchiff = int(input("Entrez votre choix: "))
        if choixchiff == 1:
            print("on va chiffrer avec notre ami cesar")
            while True:
                message_a_chiff = input("Entrez le message a chiffrer: ")
                message_a_chiff = message_a_chiff.lower()
                #print(message_a_chiff)
                """for lettre2 in message_a_chiff:
                    cara_erreur(lettre2,liste_cara_speciaux)"""
                while True:
                    decal = int(input("Entrez le decalage que vous voulez: "))
                    print("Chiffre de décalage confirmé : " + str(decal))
                    break
                
                print(CesarChiff(message_a_chiff,decal))
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ")
                nom_file = input("Qu'elle nom lui donner vous: ") 
                if file == "oui":
                    if not os.path.exists("X"):
                        os.makedirs("X")
                    if os.path.exists("X"):
                        path = "/Users/Tarkov/Desktop/general/X"
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        file1 = open(completeName, "w")
                        file1.write(CesarChiff(message_a_chiff,decal))
                        file1.close()
                else:
                    print("comme vous voudez")
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
            while True:
                message_a_chiff = input("Entrez le message a chiffrer: ")
                while True:
                    try:
                        clef = int(input("Entrez la cle de chiff que vous voulez: "))
                        break
                    except ValueError:
                        print("Mettez un chiffre !")
                print("Cle confirmé : " + str(clef))
                print(XorChiff(message_a_chiff,clef))
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
        elif choixchiff == 3:
            while True:
                print("on va chiffrer en Rsa")
                message = input('Entrez le message a chiffrer: ')
                for i in range(3):
                    print(".")
                    sleep(1)
                ####### Generation de p et q ########
                r = r.SystemRandom()
                p =liste1[r.randrange(len(liste1))]
                q = PremierDifference(p)
                n = p * q
                phi_n = (p-1)*(q-1)
                ######## Choix d'un exposant e et calcul de son inverse d ########
                e = r.choice(liste1)
                d = euclide_etendu(e, phi_n)
                print ("Cle publique :", e, "\nModulo :", n,"\nCle prive :", d)
                # n et e = cle publique, d = cle prive
                print ("\nEt voila le travail :\n", RsaChiff(message, e, n))
                print(pgcd(252,360))
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
