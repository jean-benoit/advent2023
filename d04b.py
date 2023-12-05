from collections import defaultdict


with open('data/d04.txt', 'r') as f:
    data = f.read().splitlines()

cards = defaultdict(int)
for i, line in enumerate(data):
    cards[i] += 1
    win_num = line[10:39].split()
    played = line[42:].split()
    cur = i
    for n in win_num:
        if n in played:
            cur += 1
            cards[cur] += 1 * cards[i]

print(sum(cards.values()))
# 23806951
