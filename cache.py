import math
from collections import defaultdict


class TableEntry:

    def __init__(self, set_id, tag, time_stamp):
        self.set_id = set_id
        self.tag = tag
        self.time_stamp = time_stamp


class Cache:

    def __init__(self, ways, size_of_cache, cl_size, replacement_policy):
        self.ways = ways
        self.sizeOfCache = size_of_cache
        self.cl_size = cl_size
        self.replacementPolicy = replacement_policy
        self.numSets = (size_of_cache / cl_size) / ways
        self.entries = self.numSets * ways
        self.entries_per_set = self.entries / self.numSets
        self.bitSet = math.log(self.numSets, 2)
        self.bitData = math.log(cl_size, 2)
        self.shiftAmount = self.bitSet + self.bitData
        self.lru_cache = [defaultdict(int) for sets in range(int(self.numSets))]

    def access(self, mode, address):
        my_address = int(address, 16)
        tag = my_address >> int(self.shiftAmount)
        set_id = ((my_address - (tag << int(self.shiftAmount))) >> int(self.bitData))
        entry = TableEntry(set_id, tag, 1)

        if entry.tag not in self.lru_cache[set_id].keys():
            if len(self.lru_cache[set_id]) == self.entries_per_set:
                oldest_tag = max(self.lru_cache[set_id], key=lambda time_stamp: self.lru_cache[set_id][time_stamp])
                del (self.lru_cache[set_id][oldest_tag])
                self.lru_cache[set_id].__setitem__(entry.tag, entry.time_stamp)
            else:
                self.lru_cache[set_id].__setitem__(entry.tag, entry.time_stamp)
            self.increment_time_stamp(entry, set_id)
            return False
        else:
            self.lru_cache[set_id].__setitem__(entry.tag, 0)
            self.increment_time_stamp(entry, set_id)
            return True

    def increment_time_stamp(self, entry, set_id):
        for entry.tag in self.lru_cache[set_id]:
            self.lru_cache[set_id][entry.tag] += 1





