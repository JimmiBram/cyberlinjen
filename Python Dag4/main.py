#Her hentes Operativ system biblioteket
import os, random, time

#variabler
slange_længde = 1
spiller_liv = 3
spiller_navn = ""
spiller_gæt = 0
random_tal = 0

#Funktioner
def cls():
    os.system("CLS")

def udskriv_slange(længde):
    print(">-O", end="")
    for i in range(0,længde):
        print("=", end="")
    print("")

#Jeg renser skærmen
cls()

#Velkommen
print("Velkommen til Super Slange Spillet 2025")
print("Af Jimbonator\n")

spiller_navn = input("Hvad hedder du? ")

#Selve spillet:
while spiller_liv > 0:
    cls()

    print("Din slange er nu", slange_længde, "lang og du har", spiller_liv, "liv.")
    udskriv_slange(slange_længde)

    print("Du skal gætte hvor musen er")
    print("Gæt et tal mellem 1 og 5:")
    spiller_gæt = input("")

    #Computer vælger random tal mellem 1 og 5
    random_tal = random.randint(1,5)

    cls()
    if int(spiller_gæt) == random_tal:
        print("DU GÆTTEDE RIGTIG!")
        slange_længde = slange_længde + 1
    else:
        print("DU GÆTTEDE FORKERT!")
        spiller_liv = spiller_liv - 1
    time.sleep(1.5)

cls()
print("~ GAME OVER ~")
print("Tak for spillet",spiller_navn,", din slange blev", slange_længde, "lang")
udskriv_slange(slange_længde)
