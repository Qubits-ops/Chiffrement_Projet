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
def CesarChiff(message_a_chiff, decal):
    mot_crypte = ""
    for lettre in message_a_chiff:
        mot_crypte += cryptage(decal, lettre)

    return mot_crypte
def XorChiff(str, key):
    output = ""
    for x in range(0, len(str)):
        output += chr(key ** ord(str[x]))
    return output
def genererclé(string, mdp): 
  """""Utilisez la fonction genererclé pour générer la clé. Le mot-clé est annexé à lui-même jusqu'à ce que la longueur du message soit égale à la longueur de la clé."""""
  mdp = list(mdp) 
  if len(string) == len(mdp): 
    return(mdp) 
  else: 
    for i in range(len(string) -len(mdp)): 
      mdp.append(mdp[i % len(mdp)]) 
  return("" . join(mdp)) 
  
def crypt(string, mdp):
#Une fois que le cryptage utilisé par la clé généré () pour chiffrer le message qui prend deux arguments, un est le message qui doit être crypté et  le deuxième argument est la clé qui renvoie le texte crypté.
#Dans la fonction de cryptage, le message et la clé sont ajoutés MODULO 26
  crypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(mdp[i])) % 26
    x += ord('A') 
    crypt_text.append(chr(x)) 
  return("" . join(crypt_text)) 
def decrypt(crypt_text, mdp):
#Utilisez la fonction de déchiffrement pour déchiffrer le message crypté. Cela prend deux arguments l'un est le texte crypté et le second est la clé utilisée pour le cryptage.
#Dans le texte de cryptage de la fonction de déchiffrement et la clé est soustrait, puis ajouté 26 modulo 26.
  orig_text = [] 
  for i in range(len(crypt_text)): 
    x = (ord(crypt_text[i]) -ord(mdp[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
