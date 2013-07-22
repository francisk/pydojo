class Parser(object):
    def __init__(self):
        pass

    def slice_fragement(self,input_val):
        if isinstance(input_val, list):
            return input_val[0]
        else:
            raise TypeError("Invalid input")
        

    def parse_fragment(self,input_val):
        fragement=self.slice_fragement(input_val)
        if self.is_valid_input(fragement):
            print "Parse %s" %(fragement)
            if len(input_val)>1:
                self.starter.parse_fragment(input_val[1:])
            else:
                return 
        else:
            if not self.successor is None:
                self.successor.parse_fragment(input_val)
            else:
                "Nothing could parse %s" %( str(input_val))

    def is_valid_input(self,fragement):
        pass

class StringParser(Parser):

    def __init__(self):
        Parser.__init__(self)
        
    def is_valid_input(self,fragement):
        if fragement is None:
            return True
        try:
            fragement+="test"
            return True
        except TypeError as e:
            return False

class IntegerParser(Parser):

    def __init__(self):
        Parser.__init__(self)

    def is_valid_input(self,fragement):
        if fragement is None:
            return True
        if isinstance(fragement,int):
            return True
        else:
            return False

class FloatParser(Parser):

    def __init__(self):
        Parser.__init__(self)

    def is_valid_input(self,fragment):
        if fragement is None:
            return False
        if isinstance(fragement, float):
            return True
        else:
            return False

def smoke():
    ip=IntegerParser()
    sp=StringParser()
    fp=FloatParser()
    ip.starter=ip
    sp.starter=ip
    fp.starter=ip
    ip.successor=sp
    sp.successor=fp
    ip.parse_fragment(["abc",123,456,"cdb"])

if __name__ == '__main__':
    smoke()
