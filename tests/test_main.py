import unittest

from pt_pg import main


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()