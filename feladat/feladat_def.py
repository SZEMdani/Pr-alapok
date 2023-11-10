# feladat_014
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

def nev(vnev,knev):
    print(f"A neved {vnev} {knev}. Üdvözölek téged!")

nev(vnev,knev)