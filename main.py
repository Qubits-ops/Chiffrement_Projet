import json
from chiff import *#importe notre propre bibliotheque ou il y a les fonctions de chiffrement
from plateforme import *
from math2 import *#importe notre propre bibliotheque math ou il y a les fonctions de math
from time import *#importe la bibliotheque time
import os #importe la bibliotheque os pour fournir une façon portable d'utiliser les fonctionnalités dépendantes du système d'exploitation.
#liste des nombres premiers de 101 a 997 qui sera utile pour le chiffrement RSA
import random as r
artMenu = '''
          _____                    _____                   _______                   _____                    _____                _____                            _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                 /::\    \                 /\    \                  /\    \              /\    \                          /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \               /::::\    \               /::\    \                /::\    \            /::\    \                        /::\    \                /::\____\                /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \             /::::::\    \              \:::\    \              /::::\    \           \:::\    \                      /::::\    \              /:::/    /                \:::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \           /::::::::\    \              \:::\    \            /::::::\    \           \:::\    \                    /::::::\    \            /:::/    /                  \:::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \              \:::\    \          /:::/\:::\    \           \:::\    \                  /:::/\:::\    \          /:::/    /                    \:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \              \:::\    \        /:::/__\:::\    \           \:::\    \                /:::/  \:::\    \        /:::/____/                      \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \             /::::\    \      /::::\   \:::\    \          /::::\    \              /:::/    \:::\    \      /::::\    \                      /::::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   _____   /::::::\    \    /::::::\   \:::\    \        /::::::\    \            /:::/    / \:::\    \    /::::::\    \   _____    ____    /::::::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /\    \ /:::/\:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \          /:::/    /   \:::\    \  /:::/\:::\    \ /\    \  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    |/::\    /:::/  \:::\____\/:::/__\:::\   \:::\____\    /:::/  \:::\____\        /:::/____/     \:::\____\/:::/  \:::\    /::\____\/::\   \/:::/  \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\
\::/    \:::\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / \:::\  /:::/    \::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /        \:::\    \      \::/    /\::/    \:::\  /:::/    /\:::\  /:::/    \::/    /\::/    \:::\   \::/    /\::/    \:::\   \::/    /
 \/_____/\:::\/:::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /   \:::\/:::/    / \/____/  \:::\   \:::\   \/____/   /:::/    / \/____/          \:::\    \      \/____/  \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/  \/____/ \:::\   \/____/  \/____/ \:::\   \/____/ 
          \::::::/    /         |:::::::::/    /     \:::\    /:::/    /     \::::::/    /            \:::\   \:::\    \      /:::/    /                    \:::\    \                       \::::::/    /    \::::::/    /                    \:::\    \               \:::\    \     
           \::::/    /          |::|\::::/    /       \:::\__/:::/    /       \::::/    /              \:::\   \:::\____\    /:::/    /                      \:::\    \                       \::::/    /      \::::/____/                      \:::\____\               \:::\____\    
            \::/____/           |::| \::/____/         \::::::::/    /         \::/    /                \:::\   \::/    /    \::/    /                        \:::\    \                      /:::/    /        \:::\    \                       \::/    /                \::/    /    
             ~~                 |::|  ~|                \::::::/    /           \/____/                  \:::\   \/____/      \/____/                          \:::\    \                    /:::/    /          \:::\    \                       \/____/                  \/____/     
                                |::|   |                 \::::/    /                                      \:::\    \                                            \:::\    \                  /:::/    /            \:::\    \                                                           
                                \::|   |                  \::/____/                                        \:::\____\                                            \:::\____\                /:::/    /              \:::\____\                                                          
                                 \:|   |                   ~~                                               \::/    /                                             \::/    /                \::/    /                \::/    /                                                          
                                  \|___|                                                                     \/____/                                               \/____/                  \/____/                  \/____/                                                           
                                                                                                                                                                                                                                                                                     
'''
print(artMenu)
liste100NombrePremier = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
print("detection de la plateforme en cours")
for i in range(3):
    time.sleep(1)
    print(".",end='')
print("\n")
plateforme_detect()
test = False
while test == False:
    # Demander le chemin
    path = input("rentrez le chemin ou sauvegarder le dossier qui contiendra vos message chiffrer: ")#chemin choisis ou creer le dossier stocker dans la var path
    # Si chemin == Vide alors le forcé à C:/Mes Documents par défaut
    if len(path) == 0:
        print("vous n'avez rien rentrer")
        continue
    if os.path.exists(path) == 0:
        print("chemin non existant")
        continue
    try:
        # Tente de créer le dossier
        nom_dossier = input("rentrer le nom du dossier a cree(ne rentrez pas le meme dossier que vous avez deja creer): ")
        if not os.path.exists(nom_dossier):
            os.makedirs(nom_dossier)
        test = True
    except:
        #alerte : recommencez
        continue
"""
    sauvegarde du chemin dans un json toujours pas terminer

"""
if not os.path.exists("U:\Chiffrement_Projet-main"):
    data_user = input("rentrez votre chemin: ")
    path_defaut = {"defaut":path}
    with open("preference_user.json","w") as f:
        json.dump(path_defaut,f)

else:
    print("deja existant")
filin = open("preference_user.json","r")
ligne = filin.readline()
print(ligne)
dico = json.loads(ligne)
print(dico["defaut"])
while True:#fais une boucle infinis pour tout le programme afin de redemander chaque action a l'utilisateur
    print("--------Bienvenue dans la matrix--------")
    #demande si l'user veux chiffrer dechiffrer ou stop le prog
    print("Que souhaitez-vous faire ? Tapez le chiffre correspondant")
    print("-1- Chiffrer")
    print("-2- Déchiffrer")
    print("-3- Retour")
    choix = int(input("Entrez votre choix: "))
    if choix == 1:
        #choix de l'utilisateur
        print("-1- Cesar chiffrement")
        print("-2- Xor chiffrement")
        print("-3- Rsa chiffrement")
        print("-4- Vigenere")
        print("-5- QubitChiff")
        print("-6- Substitutions Chiffrement")
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
                #demande a l'user si il veut stocker sont texte,phrase,mot crypter dans un fichier et lui demande qu'elle nom il veux lui donner
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ")
                if file == "oui":
                    nom_file = input("Qu'elle nom lui donner vous: ") 
                    #si il existe il prend le chemin du dossier et le sauvegarde a l'emplacement specifier
                    if os.path.exists(nom_dossier):
                        path += "/" + nom_dossier
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                #si le fichier existe deja il demande a l'user de saisir un autre nom pour le fichier
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        #ouvre le fichier
                        file1 = open(completeName, "w")
                        #ecrit dedans le message crypter
                        file1.write(CesarChiff(message_a_chiff,decal))
                        #ferme le fichier
                        file1.close()
                #sinon il ne fais rien si l'user refuse de sauvegarder dans un fichier
                else:
                    print("comme vous voudez")
                """chiff_copier.append(message_chiffre)
                cop =' '.join(chiff_copier)
                if cop == message_chiffre:
                print("deja chiffrer")
                break"""
                #demande a l'user si il veux arreter de chiffrer
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
                    #verifie si dnas la var clef on as bien rentrez un nombre sinon erreur
                    try:
                        clef = int(input("Entrez la cle de chiff que vous voulez: "))
                        break
                    except ValueError:
                        print("Mettez un chiffre !")
                #confirme le nombre rentrez et l'affiche a l'user
                print("Cle confirmé : " + str(clef))
                print(XorChiff(message_a_chiff,clef))
                #expliquer plus haut
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ")
                if file == "oui":
                    nom_file = input("Qu'elle nom lui donner vous: ") 
                    if os.path.exists(nom_dossier):
                        path += "/" + nom_dossier
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        file1 = open(completeName, "w")
                        file1.write(XorChiff(message_a_chiff,clef))
                        file1.close()
                #demande a l'user si il veux arreter de chiffrer
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
        elif choixchiff == 3:
            pass
        elif choixchiff == 4:
            while True:
                string = input("Entre le message: ")
                motclé = input("Entre le mot-clé: ")
                mdp = genererclé(string, motclé) 
                crypt_text = crypt(string,mdp) 
                print("Message crypter:",crypt_text) 
                print("Message decrypter:", decrypt(crypt_text, mdp))#Enfin, renvoyez les messages cryptés et déchiffrés.
                #expliquer plus haut
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ") 
                if file == "oui":
                    nom_file = input("Qu'elle nom lui donner vous: ") 
                    if os.path.exists(nom_dossier):
                        path += "/" + nom_dossier
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        file1 = open(completeName, "w")
                        file1.write(crypt_text)
                        file1.close()
                 #demande a l'user si il veux arreter de chiffrer
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
        elif choixchiff == 5:
            while True:
                message_a_chiff1 = input("rentre le message a chiffrer: ")
                cle1 = int(input("entre la cle de decalage: "))
                print(QubitChiff(message_a_chiff1,cle1))
                #expliquer plus haut
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ")
                if file == "oui":
                    nom_file = input("Qu'elle nom lui donner vous: ") 
                    if os.path.exists(nom_dossier):
                        path += "/" + nom_dossier
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        file1 = open(completeName, "w")
                        file1.write(QubitChiff(message_a_chiff))
                        file1.close()
                 #demande a l'user si il veux arreter de chiffrer
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
                """si l'utilisateur choisis 2 on dechiffre pas encore mis en place oscar fais de sont cote et moi du miens donc quand je copie sont code
                dans le projet il ya le dechiffrement du viginere dans le choix chiffrer mais on compte tout arranger quand on aura finis tous 
                les dechiffrages et tout placer dans choix 2 donc dechiffrer.
                    """
        elif choixchiff == 6:
            print("on va chiffrer par substitution")
            while True:
                message_a_chiff = input("rentre le message a chiffrer: ")
                print(substitution(message_a_chiff))
                #expliquer plus haut
                file = input("souhaitez vous sauvegarder le message chiffre dans un fichier(oui/non): ")
                if file == "oui":
                    nom_file = input("Qu'elle nom lui donner vous: ") 
                    if os.path.exists(nom_dossier):
                        path += "/" + nom_dossier
                        completeName = os.path.join(path, nom_file)
                        print("sauvegarder ici " + completeName)
                        while True:
                            if os.path.join(path):
                                if os.path.exists(nom_file):
                                    print("se fichier existe deja donner un autre nom")
                                    continue
                                break
                        file1 = open(completeName, "w")
                        file1.write(substitution(message_a_chiff))
                        file1.close()
                 #demande a l'user si il veux arreter de chiffrer
                stop = input("Voulez arreter de chiffrer(oui/non): ")
                if stop == "oui":
                    break
                elif stop == "non":
                    continue
                else:
                    print("rentrez oui ou non!")
    elif choix == 2:
        print("on va dechiffrer")
    #stop le programme si l'user decide d'arreter le programme.
    elif choix == 3:
        print("retour")
        break
    #si l'user ne fais pas les bons choix erreur
    else:
        print("choisissez 1,2,3")
        continue



