import numpy

x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
Power = x**y
Logarithm = numpy.log2(x)

print("x^y = " + str(Power))
print("log (base 2) of x = " + str(Logarithm))