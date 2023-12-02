import re

with open('data/d01.txt', 'r') as f:
    data = f.read().split('\n')
d_wrods = 'one two three four five six seven eight nine'.split()
RE = re.compile(f'(?=(\d|{"|".join(d_wrods)}))')
map = {}
for i, d in enumerate(d_wrods):
    map[d] = str(i+1)
    map[str(i+1)] = str(i+1)
total = 0
for d in data:
    digits = RE.findall(d)
    total += int(map[digits[0]] + map[digits[-1]])
print(total)
# 54265
