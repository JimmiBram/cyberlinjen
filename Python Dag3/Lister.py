#Dictionaries
konti = {
    "123456": {"balance": 5000, "pin": "1234"},
    "654321": {"balance": 3000, "pin": "5678"}
}

#Tilføj element
konti["1234"] = {"balance":2000, "pin": "1234"}

#Slet konto
del konti["123456"]

#Tjek om den eksisterer
if "123456" in konti:
    print("DEN FINDES!")
else:
    print("Den findes ikke...")

for konto in konti:
    print(konto)