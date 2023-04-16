"""bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie

author: Arnošt Raab

email: arnost.raab@gmail.com

discord: Arnošt (Arny) R.#6219"""

import random

import time
def test(testovane_cislo):
    cisilka=[]
    for index, cislice in testovane_cislo:
        if cislice == "0" and index == 0:
            return(1)
        elif cislice in cisilka:
            return(2)
        elif cislice.isdigit() != True:
            return(3)
        else:
            cisilka+=cislice
    return(0)
def bulls_cows (hodnota1, hodnota2):
    if hodnota1 > 1 or hodnota1 == 0:
        if hodnota2 > 1 or hodnota2 == 0:
            return("bulls", "cows")
        else:
            return("bulls", "cow") 
    elif hodnota1 == 1:
        if hodnota2 == 1:
            return("bull", "cow")
        else:
            return("bull", "cows")
print ("Zdravím uživateli. Zahrajeme si hru 'bulls and cows.")
print("*" * len("Zdravím uživateli. Zahrajeme si hru bulls and cows."))
print('''Krátká pravidla:
- je vygenerováno náhodné a unikátní čtyřmístné číslo, a ty se jej snažíš uhodnout
- pokud uhodneš číslici i pozici číslice, pak jde o bull(s)
- pokud uhodneš číslici, ale její pozici ne, pak jde o cow(s)
- na hádání máš max 50 pokusů, ale tolik jich snad nebude potřeba
- tvůj tip (hádané číslo) nesmí obsahovat (neobsahuje) duplicity a písmena a protože hádané číslo
  je generováno v rozmezí 1000 - 9999, tak ani tvůj tip nesmí začínat 0 (tvoje případné překlepy 
  pohlídám a upozorním tě na ně)
Hodně štěstí!!''')
print("*" * len("Zdravím uživateli. Zahrajeme si hru bulls and cows."))
chybovnik = ["zacina na 0", "opakujici se cislo", "spatny znak (pismeno)"]
nahodne_cislo = random.randint(1000, 9999)
rozlozene_cislo = tuple(enumerate(str(nahodne_cislo)))
while test(rozlozene_cislo) != 0:
    nahodne_cislo = random.randint(1000, 9999)
    rozlozene_cislo = tuple(enumerate(str(nahodne_cislo)))
pocet_pokusu = 50
start_time = time.time()
while pocet_pokusu > 0:
    print(f"Máš {pocet_pokusu} pokusu.")
    tip = input("Napiš svůj tip na čtyřmístné číslo, které si myslím!")
    rozlozeny_tip = tuple(enumerate(tip))
    if test(rozlozeny_tip) == 0:
        if nahodne_cislo == int(tip):
            print("Uhodl jsi! Výborně!")
            break
        else:
            bulls = 0
            cows = 0
            for index, prvek in rozlozeny_tip:
                for index2, prvek2 in rozlozene_cislo:
                    if prvek == prvek2 and index == index2: 
                        bulls += 1
                    elif prvek == prvek2 and index != index2:
                        cows += 1
            pocet_pokusu -= 1
            bulls_and_cows = bulls_cows(bulls, cows)
            print(f"{bulls} {bulls_and_cows[0]}; {cows} {bulls_and_cows[1]}")
    else:
        print(f"Tvůj tip nesplňuje podmínky - CHYBA:{chybovnik[test(rozlozeny_tip)-1]}")
end_time = time.time()
print("Hádání ti trvalo {} sekund".format(end_time - start_time))