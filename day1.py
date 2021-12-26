parts = open('./day1.txt').readlines()


def fuelForPart(weight):
    if weight < 8:
        return 0
    return int(weight / 3) - 2


def totalFuelForPart(weight):
    fuel = fuelForPart(weight)
    if fuel == 0:
        return 0
    return fuel + totalFuelForPart(fuel)


total = 0
for part in parts:
    total += fuelForPart(int(part))

print(total)

total = 0
for part in parts:
    total += totalFuelForPart(int(part))

print(total)
