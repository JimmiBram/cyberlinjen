import atm_funktioner

konti = {
    "123456": {"saldo": 1000, "pin": "1234"},
    "238728": {"saldo": 2000, "pin": "7777"}
}


atm_funktioner.save_list("konti.data", konti)
konti = atm_funktioner.load_list("konti.data")

konti["12345"]["saldo"]