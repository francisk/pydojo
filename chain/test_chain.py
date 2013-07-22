from chain import IntegerParser
from chain import StringParser
import unittest

class Test_StringParser(unittest.TestCase):
    def setUp(self):
        self.ip=StringParser()

    def tearDown(self):
        self.ip=None

    def test_abc_is_valid_input(self):
        self.assertTrue(self.ip.is_valid_input("abc"))
    def test_123_is_not_valid_input(self):
        self.assertFalse(self.ip.is_valid_input(1234))
    def test_none_is_not_valid_input(self):
        self.assertTrue(self.ip.is_valid_input(None))
    def test_abcd_is_current_slice(self):
        self.assertEqual("abcd",self.ip.slice_fragement(["abcd",123,"a"]))

class Test_IntergerParser(unittest.TestCase):
    def setUp(self):
        self.ip=IntegerParser()
    def tearDown(self):
        self.ip=None
    def test_123_is_valid_input(self):
        self.assertTrue(self.ip.is_valid_input(123))
    def test_abc_is_not_valid_input(self):
        self.assertFalse(self.ip.is_valid_input("abcd"))
    def test_none_is_not_valid_input(self):
        self.assertTrue(self.ip.is_valid_input(None))
        
if __name__ == '__main__':
    unittest.main()



