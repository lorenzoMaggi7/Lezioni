import random

posizione = ["_" for i in range(1, 71)]

def posizioni(tartaruga, lepre):
    for i in range(len(posizione)):
        posizione[i] = "_"
    if tartaruga == lepre:
        posizione[tartaruga - 1] = "OUCH"
    else:
        posizione[tartaruga - 1] = "T"
        posizione[lepre - 1] = "H"
    print(''.join(posizione))

def mossa_tartaruga():
    mossa = random.randint(1, 10)
    if mossa <= 5:
        return 3
    elif mossa <= 7:
        return -6
    else:
        return 1

def mossa_lepre():
    mossa = random.randint(1, 10)
    if mossa <= 2:
        return 0
    elif mossa <= 4:
        return 9
    elif mossa == 5:
        return -12
    elif mossa <= 8:
        return 1
    else:
        return -2

print("BANG !!!!! AND THEY'RE OFF !!!!!")

tartaruga = 1
lepre = 1

while True:
    posizioni(tartaruga, lepre)
    tartaruga += mossa_tartaruga()
    lepre += mossa_lepre()

    if tartaruga < 1:
        tartaruga = 1
    if lepre < 1:
        lepre = 1

    if tartaruga >= 70 and lepre >= 70:
        posizioni(tartaruga, lepre)
        print("IT'S A TIE.")
        break
    elif tartaruga >= 70:
        posizioni(tartaruga, lepre)
        print("TORTOISE WINS! || VAY!!!")
        break
    elif lepre >= 70:
        posizioni(tartaruga, lepre)
        print("HARE WINS || YUCH!!!")
        break
