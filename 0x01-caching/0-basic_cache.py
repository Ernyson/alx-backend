#!/usr/bin/env python3
"""a basic caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """base_caching sys now inherit
    """
    def put(self, key, item):
        """item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """key to retrieve an item
        """
        return self.cache_data.get(key, None)
