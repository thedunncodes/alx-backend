#!/usr/bin/env python3
""" Basic Cache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A cache system to store your data in a dictionary"""

    def __init__(self):
        """ FIFOache init method
        """
        super().__init__()
        self.counter = 0

    def put(self, key, item):
        """ Put method: adds a object into a dictionary
        with the given key and item
        """

        if key and item:
            if self.counter > self.MAX_ITEMS:
                first_key = next(iter(self.cache_data.keys()))
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                self.counter -= 2
            self.cache_data[key] = item
        self.counter += 1

    def get(self, key):
        """ get method: retreives an objece with the provided
        key
        """
        return self.cache_data.get(key) if key or key in self.cache_data else\
            None
