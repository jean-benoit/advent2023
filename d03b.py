with open('data/d03.txt', 'r') as f:
    data = f.read().splitlines()
total = 0
numbers = []
stars = []
number = ''
num_x = 0
max_x = len(data[0]) - 1

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '*':
            stars.append((x, y))
        elif char.isdigit():
            if not number:
                num_x = x
            number += char
        if number and (x == max_x or not char.isdigit()):
            numbers.append((num_x, y, number))
            number = ''

for sx, sy in stars:
    nums = []
    for nx, ny, num in numbers:
        if sx >= nx -1 and sx <= nx + len(num) and sy >= ny -1 and sy <= ny +1:
            nums.append(num)
            if len(nums) == 2:
                total += int(nums[0]) * int(nums[1])
                break
print(total)
#89471771