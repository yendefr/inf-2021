
max_count = 0
result_num = 0
for num in range(120115, 120201):
    current_count = 0
    for sep in range(1, num+1):
        if num % sep == 0:
            current_count += 1

    if current_count >= max_count:
        max_count = current_count
        result_num = num

print(max_count, result_num)
