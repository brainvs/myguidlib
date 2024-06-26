import uuid

import unittest
from myguidlib import Generator

class TestGenerator(unittest.TestCase):
    def test_generate(self):
        guid = Generator.generate()
        self.assertEqual(len(guid), 36)
        self.assertTrue(guid.count('-') == 4)

if __name__ == '__main__':
    unittest.main()