with open('data/d02.txt', 'r') as f:
    data = f.read().split('\n')
max = {'red':12, 'green':13, 'blue':14}
total = 0
for i, l in enumerate(data):
    _, boxes = l.split(':')
    ok = True
    for box_set in boxes.split(';'):
        for box in box_set.split(','):
            num, color = box.split()
            if int(num) > max[color]:
                ok = False
                break
    if ok:
        total += i + 1

print(total)
# 2716
