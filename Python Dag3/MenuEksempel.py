import atm_funktioner

while 1==1:
    atm_funktioner.clear_console()
    print("VELKOMMEN TIL MENUEN")
    print("----------------------")
    print("Hvad vil du spise?")
    print("  1. Ost")
    print("  2. Skinke")
    print("  3. Salat")
    print("  4. EXIT")

    valg = input("")
    
    print("Du valgte", valg)
    
    if(valg == "1"):
        print("OST ER OGSÅ DEJLIGT!")
    elif(valg == "4"):
        break

print("Farveller")
    