import random

cislo = random.randint(1000, 9999)
print("Random number between 0 and 10 is %s" % (cislo))
rozlozene_cislo = tuple(str(cislo))
bulls = 0
cows = 0
while (tip := int(input("Zkus uhodnout čtyřmístné číslo, které si myslím!"))) != cislo:
    rozlozeny_tip = tuple(str(tip))
    for prvek in rozlozeny_tip:
        if 
