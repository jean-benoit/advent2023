with open('data/d02.txt', 'r') as f:
    data = f.read().split('\n')

total = 0
for i, l in enumerate(data):
    max_c = {'red':0, 'green':0, 'blue':0}
    _, boxes = l.split(':')
    for box_set in boxes.split(';'):
        for box in box_set.split(','):
            num, color = box.split()
            max_c[color] = max(max_c[color], int(num))
    total += max_c['red'] * max_c['green'] * max_c['blue']

print(total)
# 72227
