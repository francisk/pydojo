from anagram import Anagram
import unittest

class Test_Anagram(unittest.TestCase):
    def setUp(self):
        self.anagram=Anagram()
    def tearDown(self):
        self.anagram=None
    def test_not_receive_string(self):
        self.assertRaises(AttributeError,self.anagram.recv,123)
    def test_ltrim(self):
        self.assertEqual('abc',self.anagram.recv(' abc').str)
    def test_rtrim(self):
        self.assertEqual('abc',self.anagram.recv('abc ').str)
    def test_trimspace(self):
        self.assertEqual('abc',self.anagram.recv(' a bc ').str)
    def test_output_list(self):
        self.assertEqual(['ab','ba'],self.anagram.recv(' a b ').ana())
    def test_output_list_3_chars(self):
        self.assertEqual(6,len(self.anagram.recv(' a bc ').ana()))
    def test_output_list_4_chars(self):
        self.assertEqual(24,len(self.anagram.recv('abcd').ana()))
    
if __name__=='__main__':
    unittest.main()
