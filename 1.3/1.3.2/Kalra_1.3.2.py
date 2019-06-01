def add_tip(total, tip_percent):
    '''Return the total amount including tip'''
    tip = tip_percent * total
    return total + tip

def hyp(leg1,leg2):
    '''Takes the square root of leg 1 squared plus leg 2 squared'''
    side1 = (leg1 ** 2)
    side2 = (leg2 ** 2)
    side3 = side1 + side2
    return side3 ** 0.5

def mean(a,b,c):
    '''Adds three numbers and takes the average of the sum'''
    mean = (a + b + c)/3.0
    return mean

def perimeter(base, height):
    '''Returns the perimeter of a rectangle'''
    perimeter = 2 * (base + height)
    return perimeter

def quadratic_expansion(a, b, c, d):
    '''(a+b)(c+d) uses the FOIL method'''
    quantity = (a * c) + (a * d) + (b * c) + (b * d)
    return quantity

#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)