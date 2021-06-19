
text = open('./24_demo.txt').read()

current_len = 0
max_len = 0
for letter in text: 
    if letter == 'Y':
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 0

if current_len > max_len:
    max_len = current_len

print(max_len)
