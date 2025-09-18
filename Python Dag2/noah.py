navn = ""

while 1==1:
    print("Choose Menu item:")
    print("1. Ændr navn")
    print("2. Print kort")
    print("3. Exit")

    valg = int(input("Menu item?:"))
    print("Du valgte:", valg)

    if valg == 1:
        navn = input("Skriv dit navn: ")
    if valg == 2:
        print("KORT: NAVN:", navn)
    if valg == 3:
        break

