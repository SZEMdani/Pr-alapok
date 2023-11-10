# feladat_015
"""
Kérjük be a vezeték és keresztnevünket.
Irassuk ki eljárás segítségével nevünket.
pl:
Be: "Kérem a vezetékneved: Szemán
Be: "Kérem a keresztneved: Dániel
Ki: "A nevem Szemán Dániel" 
"""

vnev = input("Kérem a vezetékneved: ")
knev = input("Kérem a Keresztneved: ")

def nevf(vnev, knev):
    nevem = vnev + ' ' + knev
    return nevem

print(f"A neved {nevf(vnev, knev)}. Üdvözölek téged!")