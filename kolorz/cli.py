from kolorz.colors import colors
from kolorz.kolor import kolorz
import random

def kolor():
    """
    A stand alone function to print all available colors
    """
    print("Supported colorschemes: \n")

    for color, values in colors.items():
        kol = kolorz(color)
        col = random.choice(list(values.keys()))
        print(f"{getattr(kol, col)}{color}{kol.end}")

