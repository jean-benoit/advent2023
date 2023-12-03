import re


with open('data/d03.txt', 'r') as f:
    data = f.read().splitlines()

max_x = len(data[0]) - 1
max_y = len(data) - 1
number = ''
num_x = 0
RE = re.compile(r'\d|\.')
total = 0
def check_number(x, y, number):
    return (
        (y > 0 and RE.sub('', data[y-1][max(0, x-1):min(x+len(number)+1, max_x+1)])) or
        (x > 0 and RE.sub('', data[y][x-1])) or
        (x + len(number) <= max_x and RE.sub('', data[y][x + len(number)])) or
        (y < max_y and RE.sub('', data[y+1][max(0, x-1):min(x+len(number)+1, max_x+1)]))
    )

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char.isdigit():
            if not number:
                num_x = x
            number += char
        if number and (not char.isdigit() or (char.isdigit() and x == max_x)):
            if check_number(num_x, y, number):
                total += int(number)
            number = ''
print(total)
# 556367