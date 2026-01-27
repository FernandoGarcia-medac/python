#sentencia WHILE

x = 0
while x < 20:
    if x % 2 == 0: #si el resto de dividirlo entre 2 es 0 es par
        x += 1
        continue
    if x == 15:
        break
    print(x)
    x += 1