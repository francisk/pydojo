import equeen
import unittest


class Test_8queen(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_conflict_false(self):
        self.assertFalse(equeen.conflict((3,1),4))
    def test_conflict_true(self):
        self.assertTrue(equeen.conflict((3,2),1))
    
if __name__ == '__main__':
    unittest.main()
