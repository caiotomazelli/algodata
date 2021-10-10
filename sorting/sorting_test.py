import unittest
from random import randint
from sorting import Sorting
import copy
import sys
import time

# increase recursion limit to allow for bigger test cases
sys.setrecursionlimit(int(1e5))

_CASE_LIST = [[],
              [1],
              [1,2,3],
              [9,8,7,6,5,4,3,2,1],
              [1 for _ in range(int(1e4))],
              [randint(-1e4, 1e4) for _ in range(int(1e4))]
             ]

_IMPLEMENTATION_LIST = [Sorting.qsort, Sorting.msort, Sorting.ssort, Sorting.isort]

class SortingTest(unittest.TestCase):
    def setUp(self) -> None:
        # Avoid in-place implementations to leave test cases sorted for other implementations
        self.cases = copy.deepcopy(_CASE_LIST)

    def test_sorting_works(self) -> None:
        for implementation in _IMPLEMENTATION_LIST:
            # clean-up test cases, as in-place implementations may have modified them
            self.setUp()
            start = time.time()
            for case in self.cases:
                with self.subTest(f'{implementation.__name__} sorting array of size {len(case)}'):
                    sorted_case = sorted(case)
                    self.assertListEqual(implementation(case), sorted_case)
            end = time.time()
            print(f'\n{implementation.__name__} finished cases in {(end-start):.1f} seconds.')

if __name__ == '__main__':
    unittest.main(verbosity=2) 