with open('data/d04.txt', 'r') as f:
    data = f.read().splitlines()
res = 0
for line in data:
    win_num = line[10:39].split()
    played = line[42:].split()
    winning = 0
    for n in win_num:
        if n in played:
            winning += 1
    if winning:
        res += 2**(winning-1)
print(res)
#20407