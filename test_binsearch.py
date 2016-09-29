
import unittest
from binsearch import binary_search

class MathTest(unittest.TestCase):
    
    def noindex(self):
        data = [1, 3, 5]
        self.assertEqual(binary_search(data, 3), 3, 'No index.')

    def novalue(self):
        data = [1, 3, 5]
        self.assertEqual(binary_search(collection, 299), 'Its not in the tree.', 'Its not in the tree.')

if __name__ == '__main__':
    unittest.main()
        