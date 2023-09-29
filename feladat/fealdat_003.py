# feladat_003
# dk9 95-oldal
print(f'Üdv néked!')
évek_száma = input('Hány éves vagy? ')
évek_száma = int(évek_száma)

if évek_száma == 0:
    print(f"Még nem születtél meg.")
elif évek_száma < 6:
    print(f"{évek_száma} Éves vagy. Még nem jársz általános iskolába!")
elif évek_száma >= 6 and évek_száma <= 14:
    print(f"{évek_száma} Éves vagy, általános iskolába jársz!")
elif évek_száma >= 14 and évek_száma <= 65:
    print(f"{évek_száma} Éves vagy. Vagy tanulsz, vagy dolgozol.")
elif évek_száma >= 65 and évek_száma <= 100:
    print(f"{évek_száma} éves vagy. Nyugdíjas vagy.")
elif évek_száma >= 100 and évek_száma <= 85214874587127841285645:
    print(f"{évek_száma} éves vagy. Halott vagy.")
else:
    print(f"A program nem tudta értelmezni a megadott értéket.")
