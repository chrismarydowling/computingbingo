import random

words = ['bitcoin', 'overclock', 'moor\'s law',
         'edge', 'fog', 'cloud', 'power',
         'synthesize', 'compute', 'car', 'IOT'
         'aggregate', 'distribute(d)', 'potential'
         'cluster', 'protocol', 'network', 'latency'
         'vehicle', 'node','power','smart','future'
         'diverse', 'mining', 'innovative', 'real-time'
         'portable', 'science','blockchain', 'crypto',
         'algorithm', 'big data','as a service',
         'sensorization', 'SDN', 'mobile','modular',
         'framework', 'engine','enabling','bandwidth']

print(len(words))

players = 3

out = []

for i in range(0,players):
    out.append([])
    for _ in range(0, 25):
        num = random.randint(0,len(words) - 1)
        out[i].append(words[num])


