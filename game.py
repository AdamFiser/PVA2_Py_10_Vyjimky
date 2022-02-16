#2
import random #nahrání knihovny

rozsahOd = 10
rozsahDo = 20
nahodnecislo = random.randint(rozsahOd,rozsahDo)
hledane = 0

while hledane != -1 and hledane != nahodnecislo:
    vstup = input("Zadejte číslo: ")
    hledane = int(vstup)

    if hledane == -1:  # konec hry
        print("Prohra")
        break

    elif hledane > nahodnecislo:
        print("Hledané číslo je menší.")

    elif hledane < nahodnecislo:
        print("Hledané číslo je větší")

    elif hledane == nahodnecislo:
        print("Bingo. Našel jsi číslo!")
        break

    else:
        print("Neošetřený vstup")
        continue
else:
    print("Konec")

print(f"Konec hry. Hledané číslo bylo: {nahodnecislo}.")