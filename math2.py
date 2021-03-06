import random as r #importe la bibliotheque random
#liste des nombres premiers de 101 a 997 utilie pour le chiffrement RSA
liste1 = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
# Fonction qui choisit un nombre premier different d'un autre dans la liste des nombre premier definis en haut
def PremierDifference(src:int)->int:
    diff = liste1[r.randrange(len(liste1))]
    while src == diff:
        diff = liste1[r.randrange(len(liste1))]
    return diff
#print(PremierDifference(101))
"""
Algorithme d'Euclide pour le pgcd:
le plus grand commun diviseur de deux nombres entiers non nuls est le plus grand entier qui les divise simultanément
exemple pgcd(252,360) = 36
"""
def pgcd(a:int,b:int)->int:
    while a%b != 0:
        a, b = b, a%b
    return b
