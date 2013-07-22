import unittest 
import harryport as hp

class Test_harryport(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_2_books_should_have_2_choices(self):
        self.assertEqual(2, len( list(hp.get_buying_strategies(2,5))))
    def test_3_books_should_have_4_choices(self):
        self.assertEqual(4, len( list(hp.get_buying_strategies(3,5))))
    def test_8_books_should_have_N_choices(self):
        self.assertEqual(120, len( list(hp.get_buying_strategies(8,5))))
    def test_get_stratege_price_21(self):
        self.assertEqual(22.4,hp.get_stratege_price(8,hp.DISCOUNT,
                                                 (2,1)))
    def test_get_stratege_price_51(self):
        self.assertEqual(38,hp.get_stratege_price(8,hp.DISCOUNT,(5,1)))
    def test_get_stratege_price_422(self):
        self.assertEqual(54.4,hp.get_stratege_price(8,hp.DISCOUNT,(4,2,2)))
if __name__ == '__main__':
    unittest.main()
