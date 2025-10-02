#EN LILLE ATM

#HER ER BANKENS DATA
konti = {
    "1234": {"balance": 5000, "pin": "1111"},
    "3333": {"balance": 3000, "pin": "5678"}
}

#HER ER MINE VARIABLER JEG VIL ARBEJDE MED
kunde_konto = 0
kunde_pin = 0
indtastet_pin = 0
kunde_saldo = 0

print("VELKOMMEN TIL BANKENS ATM!")
print("Skriv dit kontonummer:")

kunde_konto = input()

if kunde_konto in konti:
    #HER ER MAN KUN HVIS KONTO FINDES!
    #NU SPØRGER JEG EFTER PIN KODE
    print("Fedt, jeg har fundet dig, hvad er din pin?")
    indtastet_pin = input()
    kunde_pin = konti[kunde_konto]["pin"]

    #TJEK DET INDTASTEDE MOD KONTOENS PIN
    if indtastet_pin == kunde_pin:
        #HER ER MAN HVIS DE TO ER ENS
        print("JAAAAAAAAAAAAAA KORREKT PIN!")
    else:
        #HER ER MAN HVIS DE TO ER FORSKELLIGE
        print("NEJ FORKERT PIN!")
else:
    print("NEJ NEJ NEJ! VÆK MED DIG!")

print("FARVELLER!")