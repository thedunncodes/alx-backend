#!/usr/bin/env python3
""" Basic Cache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A cache system to store your data in a dictionary"""

    def __init__(self):
        """ LIFOCache init method
        """
        super().__init__()
        self.counter = 0
        self.last_key = False

    def put(self, key, item):
        """ Put method: adds a object into a dictionary
        with the given key and item using LIFO
        with max_no_item = 4

        this might as well be one of the cleanest
        code i've written also for FIFO
        """

        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    if not self.last_key:
                        self.last_key = list(self.cache_data.keys())[-1]
                    self.cache_data.pop(self.last_key)
                    print("DISCARD: {}".format(self.last_key))
                    self.counter -= 1
                self.cache_data[key] = item
                self.last_key = False
            else:
                self.cache_data[key] = item
                self.last_key = key
                self.counter -= 1
        self.counter += 1

    def get(self, key):
        """ get method: retreives an objece with the provided
        key
        """
        return self.cache_data.get(key) if key or key in self.cache_data else\
            None
