from random import *
from copy import *
import tkinter as tk
 
fenetre = tk.Tk()
 
photo = tk.PhotoImage(file='asciiGood.png')
 
label = tk.Label(fenetre, image=photo)
label.pack()
 
def transistor(beta:int,ic:int,ib:int):
    assert beta > 99, 'beta doit etre = a 100 au minimum'
    ie = ic + ib#courant sortant = somme courant entrant 
    ic = beta * ib
    return ie,ic
def cryptage(cle:int, lettre:str)->str:
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
 #oscar
def genererclé(string:str, mdp:str)->str: 
  """""Utilisez la fonction genererclé pour générer la clé. Le mot-clé est annexé à lui-même jusqu'à ce que la longueur du message soit égale à la longueur de la clé."""
  mdp = list(mdp) 
  if len(string) == len(mdp): 
    return(mdp) 
  else: 
    for i in range(len(string) -len(mdp)): 
      mdp.append(mdp[i % len(mdp)]) 
  return("" . join(mdp)) 
 #oscar
def crypt(string:str, mdp:str)->str:
#Une fois que le cryptage utilisé par la clé généré () pour chiffrer le message qui prend deux arguments, un est le message qui doit être crypté et  le deuxième argument est la clé qui renvoie le texte crypté.
#Dans la fonction de cryptage, le message et la clé sont ajoutés MODULO 26
  crypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(mdp[i])) % 26
    x += ord('A') 
    crypt_text.append(chr(x)) 
  return("" . join(crypt_text)) 
#oscar
def decrypt(crypt_text:str, mdp:str)->str:
#Utilisez la fonction de déchiffrement pour déchiffrer le message crypté. Cela prend deux arguments l'un est le texte crypté et le second est la clé utilisée pour le cryptage.
#Dans le texte de cryptage de la fonction de déchiffrement et la clé est soustrait, puis ajouté 26 modulo 26.
  orig_text = []
  for i in range(len(crypt_text)): 
    x = (ord(crypt_text[i]) -ord(mdp[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
def CesarChiff(message_a_chiff:str, decal:int)->str:
    """se refere a la fonction cryptage puis ajoute tous dans la variable mot crypter qui est renvoyer ensuite"""
    mot_crypte = ""
    for lettre in message_a_chiff:
        mot_crypte += cryptage(decal, lettre)

    return mot_crypte
def XorChiff(str:str, key:int)->str:
#se deplace dans l'alphabet selon chaque mot et selon une cle de decalage puis retourne une chaine de caractere avec le meme fonctionnement que chiff cesar"""
    output = ""
    for x in range(0, len(str)):
        output += chr(key ^ ord(str[x]))
    return output
    
def convertirEnBinaire(num:int)->str:
#convertis en binaire un nombre donner
    list = []
    while num > 0:
        if (num % 2) == 0:#si divisible par 2
            list.append(0)
        else:
            list.append(1)
        num//=2 #division euclidienne par 2
    return int(''.join(map(str, list[::-1])))
def QubitChiff(message_a_chiff:str)->str:
    """
    methode de chiffrement simple par Qubit
    pour dechiffrer convertir les 7 premiers bits du code binaire jusqu'a la fin
    exemple:
    11101001110101110110011000011110011 = 1110100 1110101 1101100 1100001 1110011
                                        116    117     108      97      115
    ensuite
    116 = t
    117 = u
    108 = l
    97 = a
    115 = s
    c'est le code ASCII des lettre puis on a juste a inverser le tout
    115 97 108 117 116
     s   a  l   u   t
    11101001110101110110011000011110011 = salut
    voila comment dechiffrer ma methode de chiffrement
    """
    mess = []
    mess_chiff = []
    k = []
    j = []
    for i in message_a_chiff:
        mess.append(i)
    mess = list(reversed(mess))
    for i in mess:
        mess_chiff.append(ord(i))
    for i in mess_chiff:
        k.append(convertirEnBinaire(i))
    for i in k:
        j.append(str(i))
    return "".join(j)
    #return "".join(mess)
        
#print(QubitChiff("salut"))
#oscar
def substitution(message:str)->str:
    """
        chiffrement par subsitution
    """
    alphabet = []
    for nombre in range(97,123):
        alphabet.append(chr(nombre))
    
    clef = deepcopy(alphabet)
    shuffle(clef)
    chiffrage = str()

    for lettre in message:
        chiffrage += clef[ord(lettre)-97]

    print(clef)
    return chiffrage
#print(substitution("salut"))

#oscar
def dechiffcesar(message_code):
     dict_message_decode = dict()
    # Il y'a 26 clés différentes à tester : de 0 à 25
     for cle in range(0, 26):
         dict_message_decode[cle] = CesarChiff(cle, message_code)
         
     return dict_message_decode
