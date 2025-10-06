
konti = {
    "123456": {"balance": 5000, "pin": "1234"},
    "654321": {"balance": 3000, "pin": "5678"}
}


kunde_konto = "123456"
kunde_pin = "3333"

if kunde_konto in konti:
    print("JA TAK")
    pin_for_denne_konto_er = konti[kunde_konto]["pin"]
    print("Din pinkode er:", pin_for_denne_konto_er)

