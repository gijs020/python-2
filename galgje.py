import random
global lettergeraden1
global lettergeraden2
global lettergeraden3
global fouten

lettergeraden1 = False
lettergeraden2 = False
lettergeraden3 = False
aantal_keer_geraden = 0
fouten = 0

woorden = ["aap", "vis", "jam", "alg"]
woord = random.choice(woorden)

print('welkom bij galgje.')

def checken():
    global fouten
    global lettergeraden1
    global lettergeraden2
    global lettergeraden3
    if geraden[0] == woord[0]:
        lettergeraden1 = True
    if geraden[0] == woord[1]:
        lettergeraden2 = True
    if geraden[0] == woord[2]:
        lettergeraden3 = True
    if geraden is not woord[0] and geraden is not woord[2] and geraden[0] is not woord[1]:
        print('dat is niet goed')
        fouten = fouten + 1
while True:
    if lettergeraden1 == False and lettergeraden2 == False and lettergeraden3 == False:
        print('_ _ _')
    if lettergeraden1 == True and lettergeraden2 == False and lettergeraden3 == False:
        print(woord[0], '_ _')
    if lettergeraden1 == True and lettergeraden2 == True and lettergeraden3 == False:
        print(woord[0], woord[1], '_ ')
    if lettergeraden1 == True and lettergeraden2 == True and lettergeraden3 == True:
        print(woord)
        print('je hebt het woord geraden')
        print('aantal keer geraden', aantal_keer_geraden)
        print('waarvan goed', aantal_keer_geraden - fouten)
        break
    if lettergeraden1 == False and lettergeraden2 == True and lettergeraden3 == True:
        print('_',woord[1], woord[2])
    if lettergeraden1 == True and lettergeraden2 == False and lettergeraden3 == True:
        print(woord[0], '_', woord[2])
    if lettergeraden1 == False and lettergeraden1 == True and lettergeraden3 == False:
        print('_', woord[1], '_')
    if lettergeraden1 == False and lettergeraden2 == False and lettergeraden3 == True:
        print('_ _', woord[2])
    geraden = input('noem een letter ')
    aantal_keer_geraden = aantal_keer_geraden + 1
    print('aantal fouten =', fouten)
    if fouten == 10:
        break
    checken()
