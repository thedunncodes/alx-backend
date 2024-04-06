#!/usr/bin/env python3
""" Basic Cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        """ BasicCache init method
        """
        super().__init__()

    def put(self, key, item):
        """ Put method: adds a object into a dictionary
        with the given key and item
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get method: retreives an objece with the provided
        key
        """
        return self.cache_data.get(key) if key or key in self.cache_data else\
            None
