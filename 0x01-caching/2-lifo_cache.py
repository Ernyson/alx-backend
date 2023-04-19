#!/usr/bin/python3
"""LIFO caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Now inherits from BaseCaching
    """

    def __init__(self):
        """initializes the cache"""
        super().__init__()
        self.key = ""

    def put(self, key, item):
        """key and item asigned"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                del self.cache_data[self.key]
                print(f'DISCARD: {self.key}')
            self.key = key

    def get(self, key):
        """using key to fecht data"""
        if key:
            return self.cache_data.get(key, None)
