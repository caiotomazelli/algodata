import unittest
import copy
from random import randint
from selection import Selection

_CASE_LIST = [([], 1, None),
              ([1], 1, 1),
              ([1,2,3], 3, 3),
              ([1,2,3], 4, None),
              ([9,8,7,6,5,4,3,2,1], 1, 1),
              ([1 for _ in range(int(1e4))], int(1e4), 1),
              ([1e5 - i for i in range(int(1e5))], int(1e3), 1e3)]

_IMPLEMENTATION_LIST = [Selection.quickselect]

class SelectionTest(unittest.TestCase):
    def setUp(self) -> None:
        # Avoid in-place implementations to modify test cases
        self.cases = copy.deepcopy(_CASE_LIST)

    def test_selection_works(self) -> None:
        for implementation in _IMPLEMENTATION_LIST:
            # clean-up test cases, as in-place implementations may have modified them
            self.setUp()
            for arr, k, expected in self.cases:
                with self.subTest(f'{implementation.__name__} selecting element {k} of array with len {len(arr)}'):
                    self.assertEqual(implementation(arr, k), expected) 

if __name__ == '__main__':
    unittest.main(verbosity=2)