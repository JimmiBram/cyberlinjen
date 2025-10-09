

grafik = """
\\      /
 \\    /
  \\__/
"""

kop1 = "\\      / "
kop2 = " \\ 1  /  "
kop3 = "  \\  /   "
kop4 = "    __    "


def print_kopper(antal):
    for linje1 in range(0,antal):
        print(kop1, end="")

    print("")

    for linje2 in range(0,antal):
        print(kop2, end="")

    print("")

    for linje3 in range(0,antal):
        print(kop3, end="")

    print("")

    for linje4 in range(0,antal):
        print(kop4, end="")
    
print_kopper(3)