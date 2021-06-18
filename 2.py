
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                # Вписываем сюда формулу из задания и получаем варианты переменных
                if ((x <= y) or not(w <= z)) == False:
                    print(w, x, y, z)
