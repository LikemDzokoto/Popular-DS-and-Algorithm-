from typing import Any, List
import unittest


def bin_search(arr: List[Any], target: Any) -> bool:
    """Returns true if target is in arr"""
    if len(arr) == 0:
        return False
    mid = len(arr) // 2
    if target < arr[mid]:
        return bin_search(arr[:mid], target)
    elif target > arr[mid]:
        return bin_search(arr[mid + 1:], target)
    else:
        return True


class TestBinnarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(bin_search([], 4))

    def test_item_found(self):
        self.assertTrue(bin_search([3, 4, 5, 6], 3))

    def test_odd_array_length(self):
        self.assertFalse(bin_search([0, 2, 4, 6, 8, 10, 12, 14, 16], 9))

    def test_even_array_length(self):
        self.assertTrue(bin_search([3, 4, 5, 6, 10, 20], 5))

    def test_item_not_found(self):
        self.assertFalse(bin_search([3, 4, 5, 6, 10, 20], 22))


if __name__ == '__main__':
    unittest.main()
