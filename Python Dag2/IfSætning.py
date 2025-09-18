#IF SÆTNING
#SÅDAN TJEKKES:
# ENS:              ==
# FORSKELLIG FRA:   !=
# STØRRE END:       >
# MINDRE END:       <
#Eksempel:

int_postNummer = 2000
if int_postNummer < 4999:
    landsdel = "Sjælland"
elif int_postNummer < 5999:
    landsdel = "Fyn"
elif int_postNummer < 9999:
    landsdel = "Jylland"
else:
    landsdel = "Ukendt"

print("Cool, du kommer fra", landsdel)