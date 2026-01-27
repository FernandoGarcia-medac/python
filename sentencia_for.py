#bucle for

deportes = ["futbol", "baloncesto", "tenis", "natacion", "beisbol", "voleibol", "rugby"]

for x in deportes:
    if x[0] == "f":
        continue
    elif x == "beisbol":
        break
    print(x)

