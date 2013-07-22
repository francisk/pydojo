from rental import Customer
from rental import Rental
from rental import RegularPrice
from rental import NewPrice
from rental import ChildPrice
import unittest

   
class Test_RegularPrice(unittest.TestCase):
    def setUp(self):
        self.price=RegularPrice()
    def tearDown(self):
        self.price=None
    def test_it_should_have_price_50(self):
        self.assertEqual(50,self.price.get_price(4))
class Test_NewPrice(unittest.TestCase):
    def setUp(self):
        self.price=NewPrice()
    def tearDown(self):
        self.price=None
    def test_it_should_have_a_price_120(self):
        self.assertEqual(120,self.price.get_price(4))
class Test_ChildPrice(unittest.TestCase):
    def setUp(self):
        self.price=ChildPrice()
    def tearDown(self):
        self.price=None
    def test_it_should_have_a_price_30(self):
        self.assertEqual(30,self.price.get_price(4))
class Test_Rental(unittest.TestCase):
    def setUp(self):
        self.rental=Rental()
       
    def tearDown(self):
        self.rental=None
    def test_it_should_have_a_price(self):
        custom=RegularPrice()
        self.rental.add_custom_price(custom)
        self.assertEqual(self.rental.custom_price,custom)
        
    def test_get_zero_price_when_zero_days(self):
        custom=RegularPrice()
        self.rental.add_custom_price(custom)
        self.assertEqual(0,self.rental.get_price(0))
    def test_it_shoudl_have_a_price_50_of_the_rental(self):
        custom=RegularPrice()
        self.rental.add_custom_price(custom)
        self.assertEqual(50,self.rental.get_price(4))
class Test_customer(unittest.TestCase):
    def setUp(self):
        self.cus=Customer()
    def tearDown(self):
        self.cus=None
    def test_zero_rental(self):
        self.assertEqual(0,len(self.cus.get_rentals()))
    def test_it_should_have_a_rental_list(self):
        rental=Rental()
        custom=RegularPrice()
        rental.add_custom_price(custom)
        self.cus.add_rental(rental)
        self.assertEqual(1,len(self.cus.get_rentals()))
    def test_it_should_have_a_price_50_when_given_regular(self):
        rental=Rental()
        custom=RegularPrice()
        rental.add_custom_price(custom)
        self.cus.add_rental(rental)
        self.assertEqual(50,self.cus.get_price(4))
    def test_it_should_have_a_price_200(self):
        reg_rental=Rental()
        new_rental=Rental()
        child_rental=Rental()
        reg_custom=RegularPrice()
        new_custom=NewPrice()
        child_custom=ChildPrice()
        reg_rental.add_custom_price(reg_custom)
        new_rental.add_custom_price(new_custom)
        child_rental.add_custom_price(child_custom)
        self.cus.add_rental(reg_rental)
        self.cus.add_rental(new_rental)
        self.cus.add_rental(child_rental)
        self.assertEqual(200,self.cus.get_price(4))
    def create_rental(self):
        rental=Rental()
        

if __name__ == '__main__':
    unittest.main()

    
