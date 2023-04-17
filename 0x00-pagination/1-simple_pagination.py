#!/usr/bin/env python3
"""
Simple Pagination.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    now retrieve the index range
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """
    paginating a database of popular baby names with server class
    """
    data_file = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset now
        """
        if self.__dataset is None:
            with open(self.data_file) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Now retrieve a data page
        """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        paginate_range = index_range(page, page_size)
        start, end = paginate_range[0], paginate_range[1]
        dataset = self.dataset()

        try:
            data = [dataset[i] for i in range(start, end)]
        except IndexError:
            data = []

        return data
