#!/usr/bin/env python3
"""Simple pagination.
"""

import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """Returns index start and end page for the given range
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


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
            """Returns a page of data.
            """
            assert type(page) == int and type(page_size) == int
            assert page > 0 and page_size > 0
            indexes = index_range(page, page_size)
            try:
                dataset = self.dataset()
                new_page = []
                index = indexes[0]
                index_len = indexes[1] - indexes[0]
                for i in range(index_len):
                    new_page.append(dataset[index + i])
                return new_page
            except IndexError:
                return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
            """Returns information about a page.
            """
            page_dict = {}
            dataset = self.dataset()
            data = self.get_page(page, page_size)
            try:
                page_dict['page_size'] = len(data)
                page_dict['page'] = page
                page_dict['data'] = data
                if page < ((len(dataset) + 1) // page_size):
                    page_dict['next_page'] = page + 1
                else:
                    page_dict['next_page'] = None
                if not page <= 1:
                    page_dict['prev_page'] = page - 1
                else:
                    page_dict['prev_page'] = None
                page_dict['total_pages'] = math.ceil(len(dataset) / page_size)

                return page_dict
            except IndexError:
                return {}
