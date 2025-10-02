import atm_funktioner

kontofundet = False

konti = {
    "1234": {"balance": 5000, "pin": "1234"},
    "2222": {"balance": 3000, "pin": "5678"}
}

atm_funktioner.clear_console()

atm_funktioner.print_center("INDTAST KONTO:")
kontonummer = input()
if kontonummer in konti:
    kontofundet = True
    print("JAAAA DEN FINDES")
else:
    print("NEJ FOR POKKER!")