
k = 0
for x in range(16015, 48990):
    if (x % 7 == 0 or x % 11 == 0) and x % 9 != 0 and x % 12 != 0 and x % 13 != 0:
        k += 1
        print(x)

print('Кол-во: ', k)
