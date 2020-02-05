# A Fraction class that can perform all the basic operations fractions can do: add, substract, multiply, divide

class Fraction:
    def __init__(self, top =0, bottom =1):
        # when estiablishing a fraction, check that it is reduced first
        common = self.common_denominator(top, bottom)
        top/=common
        bottom/=common
        # for calculation to work properly, the negative needs to be on the nominator
        if bottom <0:
            self.top = -top
        # denominator of a fraction cannot be zero
        elif bottom ==0:
            raise ValueError('Denominator cannot be zero')
        else:
            self.top = top

        self.bottom = bottom

    # overload the add (+) operator
    def __add__(self,X):
        # if (max(self.bottom, X.bottom))%(min(self.bottom, X.bottom))==0:
        #     sum_top = X.top+self.top
        #     sum_bottom = X.bottom
        # else:
        #     sum_top = X.top*self.bottom + X.bottom * self.top
        #     sum_bottom = self.bottom * X.bottom
        # return Fraction(sum_top,sum_bottom)
        sum_top = X.top*self.bottom + X.bottom * self.top
        sum_bottom = self.bottom * X.bottom
        return Fraction(sum_top,sum_bottom)

    #overload the substract/ minus (-) operator
    def __sub__(self,X):
        sum_top =  X.bottom * self.top - X.top*self.bottom
        sum_bottom = self.bottom * X.bottom
        return Fraction(sum_top,sum_bottom)

    #overload the multiplication (*) operator
    def __mul__(self,X):
        sum_top = self.top * X.top
        sum_bottom = self.bottom * X.bottom
        return Fraction(sum_top,sum_bottom)

    #overload the division (/) opeartor
    def __truediv__(self, X):
        sum_top = self.top * X.bottom
        sum_bottom = self.bottom * X.top
        return Fraction(sum_top,sum_bottom)
    #overload the less than (lt) < operator
    def __lt__(self,X):
        self.top *= X.bottom
        X.top *= self.bottom
        if self.top < X.top:
            return True
        else:
            return False
    #overload the greater than (gt) > operator
    def __gt__(self,X):
        self.top *= X.bottom
        X.top *= self.bottom
        if self.top > X.top:
            return True
        else:
            return False
    #overload the less than or equal to (le) <= operator
    def __le__(self,X):
        self.top *= X.bottom
        X.top *= self.bottom
        if self.top <= X.top:
            return True
        else:
            return False
    #overload the greater than or equal to (ge) >= operator
    def __ge__(self,X):
        self.top *= X.bottom
        X.top *= self.bottom
        if self.top >= X.top:
            return True
        else:
            return False
    #overload the += operator
    def __iadd__(self, X):
        return self + X
    #overload the not equal (ne)  != operator
    def __ne__(self,X):
        if (self.top!=X.top) and (self.bottom==X.bottom):
            return str(self.value()) +" not equal to "+str(X.value())
        else:
            return str(self.value()) +" equal to "+str(X.value())
        
    #overload the equal (eq) = operator
    def __eq__(self,X):
        if (self.top==X.top) and (self.bottom==X.bottom):
            return str(self.value()) +" equal to "+str(X.value())
        else:
            return str(self.value())+" not equal "+str(X.value())
    # get the numerator
    def getNum(self):
        return str(self.top)
    # get the denominator
    def getDen(self):
        return str(self.bottom)
    # get the whole fraction as numerator / denominator
    def value(self):
        return str(self.top) +"/"+str(self.bottom)
    
    # function to find the common denominar
    def common_denominator(self, x, y):
        while (x%y != 0):
            oldx =x
            oldy= y
            x= oldy
            y=oldx%oldy
        return y

#test case 1        
frac_1 = Fraction(1,5)
frac_2 = Fraction(2,5)
sum_frac_1 = frac_1+frac_2

print("frac1",frac_1.value())
print("frac2",frac_2.value())
print("frac1+frac2",sum_frac_1.value())
sum_frac_1+=frac_1
print("sum_frac+=frac1",sum_frac_1.value())

sub_frac_1 = frac_1-frac_2
print("frac1-frac2 = ",sub_frac_1.value())

div_frac_1 = frac_1/frac_2
print("frac1/frac2 = ", div_frac_1.value())

mult_frac_1 = frac_1*frac_2
print("frac1*frac2 = ",mult_frac_1.value())

#test case 2
frac_3 = Fraction(1,2)
frac_4 = Fraction(2,4)
sum_frac_2 = frac_3+frac_4
print(sum_frac_2.value())

#testing for equal
print(frac_3 == frac_4)