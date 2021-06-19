
p = range(17, 55)
q = range(37, 84)

for a in range(-500, 500):
    t = 0
    for x in range(1000):
        if (x in p) <= (((x in q) and (not(x == a))) <= (not(x in p))) == False:
            t = 1
            break
    if t == 0:
        print(a)
