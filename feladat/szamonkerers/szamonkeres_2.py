#Szemán Dániel 10.c 1.es csoport 2023.10.13

jegy = int(input("Kérek egy jegyet 1-5 ig: "))

if jegy == 5:
    print(f"A jegyed {jegy}-ös jeles!")
elif jegy == 4:
    print(f"A jegyed {jegy}-es jó!")
elif jegy == 3:
    print(f"A jegyed {jegy}-as közepes!")
elif jegy == 2:
    print(f"A jegyed {jegy}-es elégséges!")
elif jegy == 1:
    print(f"A jegyed {jegy}-es elégtelen!")
else:
    print(f"A jegyed {jegy} nem megfelelő!")