# -*- coding: utf-8 -*-
a = float(input("a = "))
while a ==0:
    print ("Error")
    a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b**2 - (4*a*c)

if D > 0:
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print ('x1 =',x1, 'x2 =', x2)
elif D == 0:
    D = -b/2*a
    print ('args x = ' , D)
else:
    print("Koreniv net")