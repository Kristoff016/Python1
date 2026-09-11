#Kérj be számokat * végjelig, és add őket össze


# osszeg = 0
# while True:
#     adat = input("Adjon meg egy számot: (* = vége): ")
#     if adat == "*":
#         break
#     else:
#         osszeg += int(adat)

# print(f"Az összeg: {osszeg}")


szamok = []
osszeg = 0
while True:
    adat = input("Adjon meg egy számot: (* = vége): ")
    if adat == "*":
        break
    else:
        szamok.append(adat)

osszeg = sum(szamok)
print(osszeg)