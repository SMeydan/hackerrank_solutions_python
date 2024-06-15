class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex(((self.real * no.real)-(self.imaginary * no.imaginary)), ((self.real * no.imaginary)+(self.imaginary * no.real)))
        
    def __truediv__(self, no):
        divisor = no.real**2 + no.imaginary**2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / divisor
        imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / divisor
        return Complex(real_part, imaginary_part)
    
    def mod(self):
        return Complex(math.sqrt(((self.imaginary**2) + (self.real**2))), 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

