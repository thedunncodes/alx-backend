#!/usr/bin/env python3
import csv
import math
from typing import Tuple, List

def index_range(page: int, page_size:int) -> Tuple:
    '''
    Returns index start and end page for the given range
    '''

    return (page * page_size, (page + 1) * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            assert page is int and page_size is int
            assert page > 0 and page_size > 0
            indexes = index_range(page, page_size)
            print(indexes)
            try:
                dataset = self.dataset()
                new_page = []
                index = indexes[0] - 2
                index_len = indexes[1] - indexes[0]
                for i in range(index_len):
                    new_page.append(dataset[index + i])
                return new_page
            except IndexError:
                 print("Page not available")


# test = index_range(page=3, page_size=4)
# print(type(test))
# print(test)

# server = Server()

# try:
#     should_err = server.get_page(-10, 2)
# except AssertionError:
#     print("AssertionError raised with negative values")

# try:
#     should_err = server.get_page(0, 0)
# except AssertionError:
#     print("AssertionError raised with 0")

# try:
#     should_err = server.get_page(2, 'Bob')
# except AssertionError:
#     print("AssertionError raised when page and/or page_size are not ints")


# print(server.get_page(1, 3))
# print(server.get_page(3, 2))
# print(server.get_page(3000, 100))
