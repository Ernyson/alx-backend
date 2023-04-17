#!/usr/bin/env python3
"""
Pagination for hypermedia

"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Paginating a database of popular baby names.
    """
    data_file = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Now cached dataset
        """
        if self.__dataset is None:
            with open(self.data_file) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        indexed by sorting position
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        Now retrieves info about a page
        """
        assert type(index) == int and index <= len(self.dataset())

        dataset = self.indexed_dataset()

        data = []
        count = 0
        for key, value in dataset.items():
            if key >= index and count < page_size:
                count += 1
                data.append(value)
                continue

            if count == page_size:
                next_index = key
                break

        res = {
            "index": index if index else 0,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }

        return res
