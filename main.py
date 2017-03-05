# -*- coding: utf-8 -*-

while True:

    try:
        a = float(input("a = "))
        if a == 0:
            print 'Error, a == 0'
            continue

        b = float(input("b = "))
        c = float(input("c = "))
    except NameError:
        print 'Incorrect data!'
        continue



    D = b ** 2 - (4 * a * c)

    if D > 0:
        x1 = (-b + D ** 0.5) / 2 * a
        x2 = (-b - D ** 0.5) / 2 * a
        print ('x1 =', x1, 'x2 =', x2)
    elif D == 0:
        D = -b / 2 * a
        print ('args x = ', D)
    else:
        print("Koreniv net")