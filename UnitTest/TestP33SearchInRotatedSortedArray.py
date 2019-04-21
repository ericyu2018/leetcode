import unittest
from Medium import P33SearchInRotatedSortedArray


class TestP33SearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.search_in_rotated_sorted_array = P33SearchInRotatedSortedArray.P33SearchInRotatedSortedArray()

    def test_search_with_existing_value(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_search_with_not_existing_value(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_search_with_boundary_value_first(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5, 6, 7, 0, 1, 2], 4), 0)

    def test_search_with_boundary_value_last(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5, 6, 7, 0, 1, 2], 2), 6)

    def test_search_in_short_list_with_boundary_value_first(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5], 4), 0)

    def test_search_in_short_list_with_boundary_value_last(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([4, 5], 5), 1)

    def test_search_in_one_element_list(self):
        self.assertEqual(self.search_in_rotated_sorted_array.search([1], 1), 0, 'haha')

    def tearDown(self):
        del self.search_in_rotated_sorted_array

if __name__ == '__main__':
    unittest.main()
