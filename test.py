import json
import os

filin = open("preference_user.json","r")
ligne = filin.readline()
dico = json.loads(ligne)
for i in dico:
    print(dico.values())
    print("voulez vous garder ce chemin pour sauvegarder votre dossier")
    choix_chemin = input("oui/non: ")
    if choix_chemin == "oui":
        print("tres bien")
        pass
    elif choix_chemin == "non":
        print("ok")
        if not os.path.exists("U:\Chiffrement_Projet-main"):
            data_user = input("rentrez votre chemin: ")
            path_defaut = {"defaut":data_user}
            with open("preference_user.json","w") as f:
                json.dump(path_defaut,f)
    else:
        print("rentrez un choix valide")
        
choix_cree_dossier = input("voulez vous créer un dossier(si pas de chemin alors dossier actuelle par defaut): ")
if choix_cree_dossier == "oui":
    nom_dossier = input("rentrer le nom du dossier a cree(ne rentrez pas le meme dossier que vous avez deja creer): ")
    if not os.path.exists(nom_dossier):
        os.makedirs(nom_dossier)
elif choix_cree_dossier == "non":
    print("d'accord")
else:
    print("rentrez un choix valide")
