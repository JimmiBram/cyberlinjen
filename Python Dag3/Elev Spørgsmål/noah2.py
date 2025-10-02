import atm_funktioner

konti = {}

fil_konti = atm_funktioner.load_list("konti.data")

if fil_konti == None:
    konti = {
        "123456": {"balance": 5000, "pin": "1234"},
        "654321": {"balance": 3000, "pin": "5678"}
    }
else:
    konti = fil_konti


#asdasdad

atm_funktioner.save_list("konti.data", konti)