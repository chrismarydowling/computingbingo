import random

words = ['bitcoin', 'overclock', 'moor\'s law',
         'edge', 'fog', 'cloud', 'power',
         'synthesize']

players = 3

out = []

for i in range(0,players):
    # select 25 random words
    out.append([])
    for _ in range(0, 25):
        num = random.randint(0,len(words) - 1)
        out[i].append(words[num])

print(len(out[2]))


