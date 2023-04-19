#!/usr/bin/python3
"""FIFO Caching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class that inherits from
    BaseCaching
    """

    def __init__(self):
        """initializes the cache
        """
        super().__init__()
        self.load = []

    def put(self, key, item):
        """item in cache
        """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.load.append(key)
            else:
                self.cache_data[key] = item
                discard = self.load[0]
                del self.cache_data[self.load[0]], self.load[0]
                self.load.append(key)
                print(f'DISCARD: {discard}')

    def get(self, key):
        """now get a key from the cache
        """
        if key:
            return self.cache_data.get(key, None)
