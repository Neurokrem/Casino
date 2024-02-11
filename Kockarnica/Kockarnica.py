import random

MAX_LINIJA = 3
MAX_OKLADA = 100
MIN_OKLADA = 1

REDAK = 3
STUPAC = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def uvjet_pobjede(stupci, linije, oklada, vrijednosti):
    pobjede = 0
    pobjedne_linije = []
    for linija in range(linije):
        simbol = stupci[0][linija]
        for stupac in stupci:
            symbol_to_check = stupac[linija]
            if simbol != symbol_to_check:
                break
        else:
            pobjede += vrijednosti[simbol] * oklada
            pobjedne_linije.append(linija + 1)
    return pobjede

def get_slot_machine_spin(redak, stupac, simboli):
    svi_simboli = []
    for simbol, symbol_count in simboli.items():
        for _ in range(symbol_count):
            svi_simboli.append(simbol)

    stupci = []
    for _ in range(stupac):
        stupac = []
        trenutni_simboli = svi_simboli[:]
        for _ in range(redak):
            value = random.choice(trenutni_simboli)
            trenutni_simboli.remove(value)
            stupac.append(value)

        stupci.append(stupac)
    return stupci

def print_slot(stupci):
     #transponiranje matrice
     for red in range(len(stupci[0])):
        for i, stupac in enumerate(stupci):
            if i != len(stupci) -1:
                print(stupac[red], end=" | ")
            else:
                print(stupac[red], end="")
        print()

def depozit():
    while True:
        iznos = input("Koliki je vaš depozit? ")
        if iznos.isdigit():
            iznos = int(iznos)
            if iznos > 0:
                break
            else:
                print("Iznos mora biti veći od nule!")
        else:
            print("Molimo unesite broj.")
    return iznos

def broj_redaka():
    while True:
        redak = input("Koliko linija oklade (1-"+ str(MAX_LINIJA) + ")? ")
        if redak.isdigit():
            redak = int(redak)
            if 1 <= redak <= MAX_LINIJA:
                break
            else:
                print("Broj redaka mora biti između 1 i 3!")
        else:
            print("Molimo unesite broj.")
    return redak

def daj_okladu():
    while True:
        oklada = input("Koliko se kladite na svakom retku? ")
        if oklada.isdigit():
            oklada = int(oklada)
            if MIN_OKLADA <= oklada <= MAX_OKLADA:
                break
            else:
                print(f"Iznos mora biti između {MIN_OKLADA}€ - {MAX_OKLADA}€")
        else:
            print("Molimo unesite broj.")
    return oklada

def igra(balans):
    redak = broj_redaka()
    while True:
        oklada = daj_okladu()
        ukupna_oklada = oklada * redak
        if ukupna_oklada > balans:
            print(f"Nemaš dovoljno novaca za klađenje! Vaš balans je {balans}€")
        else:
            break
    
    print(f"Kladiš se na {oklada}€ na {redak} linija. Ukupni iznos oklade je {ukupna_oklada}€")
    slots = get_slot_machine_spin(REDAK, STUPAC, symbol_count)
    print_slot(slots)
    pobjede = uvjet_pobjede(slots, redak, oklada, symbol_value)
    print(f"Osvojio si {pobjede}€")
    #print(f"Pogodio si retke:", *pobjedne_linije)
    return pobjede - ukupna_oklada

#### Ovdje je glavna funkcija ####
def main():
    balans = depozit()
    while True:
        print(f"Trenutačni iznos: {balans}€")
        odgovor = input("Pritisni ENTER za novu igru (q za izlaz)")
        if odgovor == "q":
            break
        balans += igra(balans)
        if balans == 0:
            break
    print(f"Otišli se s {balans}€. Ugodan dan!")
  
if __name__ == "__main__":
    main()