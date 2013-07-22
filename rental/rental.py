class Customer(object):
    """
    """
    
    def __init__(self):
        self._rental_list=[]
    def add_rental(self,rental):
        self._rental_list.append(rental)
    def get_rentals(self):
        return self._rental_list
    def get_price(self,days_rent):
        result=0
        for rental in self._rental_list:
            result+=rental.get_price(days_rent)
        return result
   
class Rental(object):
    def __init__(self):
        self.custom_price=None
        
    def get_price(self,rental_days):
        return self.custom_price.get_price(rental_days)                                           
    def add_custom_price(self,custom):
        self.custom_price=custom
        
    @property
    def custom(self):
        return self.custom_price
    
class CustumePrice(object):
    def __init__(self):
        pass

    def get_price(self,days_rent):
        pass
    
class RegularPrice(CustumePrice):
    def __init__(self):
        CustumePrice.__init__(self)
        
    def get_price(self,days_rent):
        if days_rent in range(1,3):
            return 20
        elif days_rent>2:
            return 20 + (days_rent-2)*15
        elif days_rent==0:
            return 0
class NewPrice(CustumePrice):
    def __init__(self):
        CustumePrice.__init__(self)

    def get_price(self,days_rent):
        return 30*days_rent


class ChildPrice(CustumePrice):
    def __init__(self):
        CustumePrice.__init__(self)

    def get_price(self,days_rent):
        if days_rent in range(1,4):
            return 15
        elif days_rent > 3:
            return 15 + (days_rent-3)*15
