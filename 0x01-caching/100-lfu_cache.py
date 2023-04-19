#!/usr/bin/env python3
"""
Least Frequently Used - LFU caching
"""
BaseCaching = __import__('base_caching').BaseCaching

from collections import OrderedDict

import operator


class LFUCache(BaseCaching):
    """
    Now inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.freq = OrderedDict()
        self.sorted = None

    def put(self, key, item):
        """
        Add key and item
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.freq:
            self.sorted = sorted(self.freq.items(), key=operator.itemgetter(1))
            discard = self.sorted.pop(0)[0]
            del self.freq[discard]
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            val = 0
            if key in self.cache_data:
                val = self.freq[key]
                del self.freq[key]

            self.freq[key] = val + 1
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve item with key
        """
        if not key or key not in self.cache_data:
            return None

        val = 0
        if key in self.freq.keys():
            val = self.freq[key]
            del self.freq[key]

        self.freq[key] = val + 1
        return self.cache_data[key]
