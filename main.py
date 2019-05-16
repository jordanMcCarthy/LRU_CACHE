import sys
from cache import Cache

traceFile = open(sys.argv[1], "r")
c = Cache(16, 1048576, 64, "LRU")
hit = 0
miss = 0
total = 0

for line in traceFile:
    total += 1
    fields = line.split(" ")
    mode = fields[1]
    address = fields[2]
    result = c.access(mode, address)
    if result is True:
        hit += 1
    else:
        miss += 1

miss_rate = float(miss) / float(total)
miss_rate_percentage = miss_rate * 100
print ('Cache miss rate: %.2f%%'%miss_rate_percentage )










