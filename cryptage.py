# constantes:
import base64

cle = [17, 5,5]  # [a(compris entre 2 et 20), b , c]   !!cle n'est pas une constante mais pratique pour l'exercice !!
BASE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def help():
    a = ('''
    Library by Corentin Vaillant, 
    if you have any question or isues contact me on discord or github please :
        discord :   kokoquelicot#0593
        github :    CorentinVaillant
    
    -use crypt to crypt a word with a keycode:
        crypt(YourWord, YourKeycode)
    -use cryptLong to crypt a longer word or a sentence :
        cryptLong(YourSentence, YourKeycode)
    
    -you can reversed it with the unCrypt or unCryptLong fonction
    
    /!\your keycode must be a list of thre integer, you can use a default one with the variable 'cle'/!\ 
    ''')
    print(a)
    return (a)


def crypt(mot, cle):
    lettres = list(mot)
    lettres = [format(ord(i), '08b') for i in lettres]  # convertion binnaire

    for l in range(len(lettres)):
        # inversion 0 et 1
        lettres[l] = lettres[l].replace('0', 'o')
        lettres[l] = lettres[l].replace('1', '0')
        lettres[l] = lettres[l].replace('o', '1')

        lettres[l] = ''.join(reversed(lettres[l]))  # changement sens

        lettres[l] = int(lettres[l], 2)  # conversion en int

        lettres[l] = lettres[l] + cle[1] + cle[2] * (cle[0] ** l)  # ajout de la clée2 (plus clée 3 à chaque lettre)

        lettres[l] = baseN(lettres[l], cle[0] + l)  # changement base selon clé 1

        lettres[l] = int(lettres[l], 36)  # convertion en base 36

    return (lettres)


def unCrypt(lettres, clee):
    for l in range(len(lettres)):
        lettres[l] = baseN(lettres[l], 36)

        lettres[l] = int(lettres[l], clee[0] + l)  # changement base selon clé 1

        lettres[l] = lettres[l] - cle[1] - cle[2] * (
                    cle[0] ** l)  # soustraction de la clée2 (plus clée 3 à chaque lettre)

        lettres[l] = '{0:08b}'.format(lettres[l])  # convertion bin

        lettres[l] = ''.join(reversed(lettres[l]))  # changement sens

        # inversion 0 et 1
        lettres[l] = str(lettres[l])
        lettres[l] = lettres[l].replace('1', 'o')
        lettres[l] = lettres[l].replace('0', '1')
        lettres[l] = lettres[l].replace('o', '0')
        lettres[l] = int(lettres[l], 2)

        lettres[l] = chr(lettres[l])  # convertion char

    return ''.join(lettres)


def baseN(n, b):
    reste = ""
    while n:
        #print(n)
        reste += BASE[n % b]
        n //= b
    return reste[::-1] or "0"


def motALaBonneTaille(phrase):
    if type(phrase) == str:
        li = False
    elif type(phrase) == list:
        li = True
    else:
        print('error, not a list or a string !'); quit()
    mots = []
    phrase = list(phrase)
    while len(phrase) > 10:
        if li:
            mots.append((phrase[:11]))
        elif not li:
            mots.append(''.join(phrase[:11]))
        del phrase[:11]

    if li:
        mots.append((phrase[:11]))
    elif not li:
        mots.append(''.join(phrase[:11]))
    return mots


def cryptLong(mot, cle):
    phrase = []
    mot = motALaBonneTaille(mot)
    for k in mot:
        phrase.append(crypt(k, cle))
    return phrase


def unCryptLong(mot, cle):
    phrase = []
    for k in mot:
        phrase.append(unCrypt(k,cle))
    return ''.join(phrase)


#test
def test():
    print("crypt('test',cle):",crypt('test',cle))
    print("unCrypt(crypt('test',cle),cle):",unCrypt(crypt('test',cle),cle))

    print (cryptLong('test il s agit du mot exprimant la focntion d une expérience ayant pour but d experimenter ', cle))
    print(unCryptLong(cryptLong("test il s'agit du mot exprimant la focntion d'une expérience ayant pour but d'experimenter", cle),cle))
    print('all the functions works !!')
