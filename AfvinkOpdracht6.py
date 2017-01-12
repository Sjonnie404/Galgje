# Auteur:       Shane Pullens
# Doel:         Spel galgje nabootsen
# Datum:        07-01-2016
# Versie:       1.0

#Imports:
from random import randint
#



def main():
    leesfile("woorden.txt")
    kieswoord()
    lengte()
    keuze()

Galgje = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

def leesfile(bestand):
    lijst = []
    try:
        file = open (bestand,'r')
        for regel in file:
            regel = regel.replace("\n","")
            lijst.append(regel)
        return lijst
    except FileNotFoundError:
        print ("Bestand niet gevonden!")

def random():
    r = randint(0,95)
    print (r)
    return r

def kieswoord():
    random1 = random()
    lijst = leesfile("woorden.txt")
    woord = (lijst[random1])
    return (woord)

def lengte():
    woord = kieswoord()
    aantal = ("_ "*len(woord))
    print (aantal)
    return aantal

def keuze():
    woord = kieswoord()
    aantal = lengte()
    fout = -1
    print (woord)
    for x in woord:
        
        gok = input("Geef een letter:")
        if gok in woord:
            print ("Goedzo, deze letter komt voor in het woord!")
            
        else:
            print ("Helaas, deze letter komt niet in het woord voor.")
            fout =(fout + 1)
            print ("Je hebt er nu zoveel fout(en):" , fout)
            print (Galgje[fout])



main()
