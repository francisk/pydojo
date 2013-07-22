class Anagram(object):
    """
    """
    
    def __init__(self):
        self.str=''
        self.output=[]
        
    def recv(self,input):
        if not isinstance(input,str):
            raise AttributeError('Please input a string')
        self.str=''.join(input.strip().split(' '))
        return self
    
    def ana(self):
        self._generate_output(self.str,'')
        return self.output
        
    def _generate_output(self,input_str,tmp_str):
        for char in input_str:
            pos=input_str.index(char)
            if len(input_str)-1>0:
                str_left=input_str[:pos]+input_str[pos+1:]
                self._generate_output(str_left,tmp_str+char)
            else:
                self.output.append(tmp_str+char)

class AnaLst(object):
    def __init__(self, number):
        self._number = number

    def render(self,given,tmp):
        if len(given)>1:
            for num in given:
                pos=given.index(num)
                left=given[:pos]+given[pos+1:]
                for result in self.render(left,tmp+(num,)):
                   yield result + (num,)
        else:
            yield (given,)
     

def smoke():
    l=AnaLst(123)
    lst=l.render([1,2,3,4],())
    print len(list(lst)) 
if __name__ == '__main__':
    smoke()
