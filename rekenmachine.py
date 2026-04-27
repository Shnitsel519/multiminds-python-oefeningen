getal1 = float(input("Eerste getal: "))
getal2 = float(input("Tweede getal: "))

print(f"{getal1} + {getal2} = {getal1 + getal2}")
print(f"{getal1} - {getal2} = {getal1 - getal2}")
print(f"{getal1} * {getal2} = {getal1 * getal2}")
if getal2 != 0:
    print(f"{getal1} / {getal2} = {getal1 / getal2:.2f}")
else:
    print("Delen door nul is niet mogelijk.")
    