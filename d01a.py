import re

with open('data/d01.txt', 'r') as f:
    data = f.read().split('\n')
total = 0
for inp in data:
    digits = re.sub('\D','', inp)
    total += int(digits[0] + digits[-1])
print(total)