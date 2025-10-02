#ATM OPGAVE DAG
#FUNKTIONER
#DICTIONARIES
#JSON
#FILER

def UdskrivSaldo(unavn, ukonto, usaldo):
    print("Kære ", unavn)
    print("Din konto", ukonto, " har dette beløb:")
    print(usaldo, ",- DKK")

navn = "Hans Hansen"
konto = 1234
saldo = 1000

UdskrivSaldo(navn, konto, saldo)
print("Nu snupper jeg 500!")
saldo = saldo - 500
UdskrivSaldo(navn, konto, saldo)