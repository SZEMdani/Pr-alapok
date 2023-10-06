"""
Kérjünk be két egész számot, szám1 és szám2
hasonlitsuk össze a két számot, és irassuk ki, hogy
a szám1 kisebb mint a szám2, vagy a szám2 kisebb mint a szám1, vagy a szám1 egyenlő
szám2-vel.
"""
szám1=input("írj be egy számot /szám1/ : ")
szám2=input("írj be mégegy számot /szám2/ : ")
szám1=int(szám1)
szám2=int(szám2)

if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint szám1")
elif szám1 == szám2:
    print(f"A szám1 egyenlő a szám2-vel")

"""
if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
if szám2 < szám1:
    print(f"A szám2 kisebb mint szám1")
if szám1 == szám2:
    print(f"A szám1 egyenlő a szám2-vel")
"""