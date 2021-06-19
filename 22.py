
for x in range(1000, 10000):
    a, b = 0, 1
    x_input = x
    while x > 0:
        a = a + 1
        b = b * (x%1000)
        x = x//1000
    if a == 2 and b == 11:
        print(x_input)
