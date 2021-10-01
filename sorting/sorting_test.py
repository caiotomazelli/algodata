import unittest
from random import randint
from sorting import Sorting
import copy

_CASE_LIST = [[],
              [1],
              [1,2,3],
              [9,8,7,6,5,4,3,2,1],
              [1 for _ in range(int(1e2))],
              [randint(-1e2, 1e2) for _ in range(int(1e2))]
             ]

_IMPLEMENTATION_LIST = [Sorting.qsort]

class SortingTest(unittest.TestCase):
    def setUp(self) -> None:
        # Avoid in-place implementations to leave test cases sorted for other implementations
        self.cases = copy.deepcopy(_CASE_LIST)

    def test_sorting_works(self) -> None:
        for implementation in _IMPLEMENTATION_LIST:
            for case in self.cases:
                with self.subTest(f'{implementation.__name__} sorting array of size {len(case)}'):
                    sorted_case = sorted(case)
                    self.assertListEqual(implementation(case), sorted_case)

if __name__ == '__main__':
    unittest.main()