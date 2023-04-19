#!/usr/bin/env python3
"""FIFO Caching
"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching



class FIFOCache(BaseCaching):
    """class that inherits from
    BaseCaching
    """
    def __init__(self):
        """Initialize
        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """now get a key from the cache
        """
        return self.cache_data.get(key, None)
