#imports:
import atm_funktioner

#variabler:
kunde_kontonummer = 0
kunde_saldo = 0
kunde_pinkode = 0

#data
konti = {
    "123456": {"balance": 5000, "pin": "1234"},
    "654321": {"balance": 3000, "pin": "5678"}
}

#logik
print("Hej kunde, hvad er dit kontonummer?")
kunde_kontonummer = input()

print("Godt, hvad er så din pin kode?")
kunde_pinkode = input()

