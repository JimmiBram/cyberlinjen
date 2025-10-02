#DENNE FIL SKAL I BRUGE I JERES ATM PROJEKT!
#DEN INDEHOLDE VIGTIGE FUNKTIONER I KAN BRUGE

import os
import shutil
import json

def clear_console():
    if os.name == "nt":   # Windows
        os.system("cls")
    else:                 # Linux og macOS
        os.system("clear")

def print_center(text: str, newlines: int = 0) -> None:
    """Printer tekst centreret i konsollen med valgfri ekstra tomme linjer bagefter."""
    width = shutil.get_terminal_size().columns
    print(text.center(width))
    if newlines > 0:
        print("\n" * newlines, end="")

def save_list(filename, listcontent):
    """Gemmer en liste (eller dict) til en JSON-fil."""
    with open(filename, "w") as f:
        json.dump(listcontent, f)

def load_list(filename):
    """Indlæser en liste (eller dict) fra en JSON-fil."""
    with open(filename, "r") as f:
        return json.load(f)