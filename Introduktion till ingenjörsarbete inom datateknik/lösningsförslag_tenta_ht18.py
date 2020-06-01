import math
import random

# Question 1
# -----------------
'''
# Original function.
def listDivision(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i] / y[i])
    return z
'''
# Fixed function.
def listDivisionFixed(x, y):
    z = []
    
    for i in range(len(x)):
        try:        
            z.append(int(x[i] / y[i]))
        except ZeroDivisionError as e:
            print("One problem -", "ZeroDivisionError:", e, "when i =", i)
        except IndexError as e:
            print("Another problem -", "IndexError:", e, "when i =", i)
    return z


# Question 2 
# -----------------
def reverse_for(s):
    r = ""  # Empty result string.
    
    # Strings are iterable, so let's iterate over all chars..
    for ch in s:
        r = ch + r   # ...and add each char to the *beginning* of the result string.
   
    '''
    # Alt.:
    for i in range(len(s)):
        r = s[i] + r
   
    # ...or:
    for i in range(len(s)-1, -1, -1):
        r += s[len(s)-1]
    '''

    return r   # ...and, of course, return the result.


# Question 3
# -----------------
def reverse_while(s):
    r = ""
    
    i = 0  # For a while loop, we need an extra variable... 
    while i < len(s):
        r = s[i] + r
        i = i + 1   # ...which must be changed for each iteration.

    '''
    # Alt.:
    i = len(s) - 1
    while i >= 0: 
        r += s[i]
        i -= 1
    '''

    return r


# Question 4
# -----------------
def LCD(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        d = n1
        while (d % n2) > 0:
            d = d + n1
        return d
    else:
        d = n2
        while (d % n1) > 0:
            d = d + n2
        return d   # Notice, the LCD will not be calculated *correctly* with...
                   # ...this return (or the return above) indented into the while loop.


# Question 5
# -----------------
def func(lst, n):
    for i in range(2, n):
        if n % i == 0:
            return   # Notice, a 'return' will unconditionally break the function...

    # 'n' will, therefore, not be appended to the list in case 'n' is...
    # ...evenly divisible by another number in the interval [2, n).
    lst.append(n)

    # ...and yes, I know that this was a tricky question.


# Question 6
# -----------------
# This question was about recursive functions.
# An answer without recursion is, therefore, equal to 0 points.
# -----------------
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1

'''
Alt.:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
'''


# Question 8
# -----------------
def testInterval(x, txt):
    print('x =', x, '-- answers', txt, 'interval:', end=' ')
    if x >= 0.0 and x <= 1.0:
        print('a', end=' ')
    if x >= 0.0 or x <= 1.0:
        print('b', end=' ')
    if x in [0.0, 1.0]:
        print('c', end=' ')
    if x > 0.0 or x < 1.0:
        print('d', end=' ')


# Question 10 
# -----------------
def splitStr(x, y, z):
    txt = 'pythons are snakes'
    words = txt.split(' ')
    print(words[z][y] + words[y][z] + words[x][z])


# Question 11 
# -----------------
class ComplexNumber:

    # Q11 a). 
    # It is the keyword 'self' that is used to indicate that a method...
    #  ...or variable is a member of the class.
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def addReal(self, r):
        self.real += r

    def addImag(self, i):
        self.imag += i

    def __add__(self, c):
        return ComplexNumber(self.real + c.real, self.imag + c.imag)

    def __str__(self):
        return "{0} + {1}j".format(self.real,self.imag)

# ---------------
# Main function
# ------------------
if __name__ == "__main__":
    
    print('\nQuestion 1:')
    a = [1, 8, 9, 5, 16, 24, 0, 8]
    b = [1, 2, 3, 0, 4, 6, 5]
    c = listDivisionFixed(a, b)
    print(c)

    print('\nQuestion 2:')
    s = 'hello world'
    r = reverse_for(s)
    print(r)

    print('\nQuestion 3:')
    s = 'hello world'
    r = reverse_while(s)
    print(r)

    '''
    # ...and here is also the most optimal solution (as pointed out by some of you):
    r = s[::-1]
    print(r)
    '''

    print('\nQuestion 4:')
    n1, n2 = 3, 8
    lcd = LCD(n1, n2)
    print("LCD:", lcd)

    print('\nQuestion 5:')
    lst = []
    for i in range(10, 20):
        func(lst, i)
    print(lst)

    print('\nQuestion 6:')
    n = 5
    print("my factorial:", factorial(n))
    print("math.factorial:", math.factorial(n))

    print('\nQuestion 7:')
    for i in range(1, 10, 2):
        print(i, end=' ')   

    print('\n\nQuestion 8:')
    x = [0.999, 1.0, 1.001]
    txt = ['within', 'within (upper boundary)', 'outside']
    for i in range(len(x)):
        testInterval(x[i], txt[i])
        print('')

    print('\nQuestion 9:')
    print("a) 27 / 3 / 3 =", (27 / 3 / 3))
    print("b) math.sqrt(9) =", math.sqrt(9))
    print("a) 9 ** (1/2) =", (9 ** (1/2)))
    print("d) 27 % 3 =", (27 % 3))

    print('\nQuestion 10:')
    splitStr(-1, 1, -3)

    print('\nQuestion 11:')
    c1 = ComplexNumber(2, 3)
    c1.addReal(2)
    c2 = c1          # Notice, objects are assigned by references... 
    c2.addImag(1)    # ...so changes to c2 will also be reflected in c1.
    print(c1)

    print('\nQuestion 12:')
    if True:
        print("a) This is within an 'if' which is *not* accompanied by an 'else'.")
    
    print('\nQuestion 13:')
    X = {'A': 1, 'C': 2, 'B': 3, 4: 'D', 'E': 5}
    for k in X.keys():
        print(X[k], end=' ')

    print('\n-------------------')
    
