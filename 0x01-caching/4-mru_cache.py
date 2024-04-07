#!/usr/bin/env python3
""" MRU Cache class
https://en.wikipedia.org/wiki/Cache_replacement_policies
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ A cache system to store your data in a dictionary
    and also retrieve it

    NOTE: The rank system in MRU system doesn't just work
    for data inputs but also for retrieveing data also,
    so rank of stored objects increase as your input and
    request a data

    Nah This is the cleanest, its the opposite of lru,
    but implemnted with minimal changes, just a variable or 2
    """

    def __init__(self):
        """ MRUCache init method
        """
        super().__init__()
        self.rank_dict = {}
        self.rank = 0
        self.rank_values = []

    def get_highest_key(self, search_value: int):
        """ Method to return the highest ranked
        key in the MRU dict
        """
        key, value = [], []
        for k, v in self.rank_dict.items():
            key.append(k)
            value.append(v)
        search_index = value.index(search_value)

        return key[search_index]

    def put(self, key, item):
        """ Put method: adds a object into a dictionary
        with the given key and item
        """

        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.rank_values = list(self.rank_dict.values())
                    highest_key = self.get_highest_key(max(self.rank_values))
                    self.cache_data.pop(highest_key)
                    self.rank_dict.pop(highest_key)
                    print("DISCARD: {}".format(highest_key))
                self.cache_data[key] = item
                self.rank_dict[key] = self.rank
                self.rank += 1
            else:
                self.cache_data[key] = item
                self.rank_dict[key] = self.rank
                self.rank += 1

    def get(self, key):
        """ get method: retreives an objece with the provided
        key
        """

        if key in self.rank_dict:
            self.rank_dict[key] = self.rank
        self.rank += 1
        return self.cache_data.get(key) if key or key in self.cache_data else\
            None
