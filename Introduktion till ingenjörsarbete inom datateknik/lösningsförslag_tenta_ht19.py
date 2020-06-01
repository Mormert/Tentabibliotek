from time import time
import math

# Question 1
# ------------------------------------------------------
#  Note, since this is an 'if-elif-else' statement, only 
#  one "branch" (and one branch only) will be executed, i.e.
#  the code block of the *first* 'if-elif' statement that is
#  true (or the code block of the 'else' statement in case
#  none of the above 'if-elif' statements are true).
# ------------------------------------------------------
def selector(x):
    if x > 1 and x < 4:
        print("A", end=" ")  # Note, "end" parameter is here used to  
                             # ...override default newline.  
    elif x == 2:
        print("B", end=" ")

    elif x > 2 and x <= 4:
        print("C", end=" ")

    else:
        print("D", end=" ")


# Question 2
# --------------------------
def caesarCipher(txt, shift):
    cipher = ""
    for ch in txt:
        x = ord(ch) + shift
        cipher = cipher + chr(x)
    return cipher
    ''''    
    alt. 
    cipher = ""
    i = 0
    while i < len(txt):
        x = ord(txt[i]) + shift
        cipher = cipher + chr(x)
        i += 1
    return cipher
    '''

# Question 3
# --------------------------
class Timing:
    
    # a) This '__init__' class method is the "class construtor", which is called 
    #    each time an object of the class is instantiated, e.g., line 164.
    def __init__(self):
        self.t = time()

    def reset(self):
        self.t = time()

    def stop(self):
        self.t = time() - self.t

    def log(self, msg):
        print("{0}: {1:0.3f}".format(msg, self.t))


# Question 4
# --------------------------
def sort(x):
    '''
    Original sort function with the use of for loops:
    --------------------------------------------------
    for i in range(0, len(x)):
        for j in range(i, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i] 
    '''
    i = 0
    while i < len(x):
        j = i
        while j < len(x):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
            j += 1
        i += 1
        

# Question 5
# --------------------------
def mean(x):
    i, sum = 0, 0
    N = len(x)
    while i < N:
        sum += x[i]
        i += 1
    return sum / N

def std(x):
    i, sum = 0, 0
    N = len(x)
    while i < N:
        sum += pow(abs(x[i] - mean(x)), 2)
        i += 1
    return math.sqrt(sum / N)


# Question 6
# --------------------------
def str2intA(s):
    try:
        i = int(s)
        return i
    except ValueError as e:
        return 0

def str2intB(s):
    i = eval(s)
    if type(i) != int:
        i = round(i)
    return i


# Question 8
# -------------------------        
def fatalStr(x, y):
    txt = "fatal system error"
    return txt.split(" ")[x][y] + txt.split(" ")[y][x]


# Question 9
# -------------------------        
def exp(x, y):
    if (x and not y) or (not x and y):
        return True
    return False


# Question 10
# -------------------------        
def factorial(n):
    if n == 1:  # Base case: a)
        return 1
    return n * factorial(n - 1)


# Question 3
# --------------------------------------------------------------------
# b) The condition below is *only true* in case the script is executed
#    as a "stand alone script" and not if the script is "imported as
#    a library script", i.e., the code in the "main" condition is
#    only executed if the script is directly executed.
# -------------------------
if __name__ == "__main__":

    print("Q1:")
    for i in range(5):
        selector(i)

    print("\n\nQ2:")
    txt = "birds are no snakes"
    encrypted = caesarCipher(txt, 12)
    print(encrypted)
    decrypted = caesarCipher(encrypted, -12)
    print(decrypted)
    
    print("\nQ3:")
    t = Timing()
    even = []
    t.reset()
    for num in range(100000): # 10000000
        if num % 2 == 0: 
            even.append(num*num)
    #t.stop()
    #t.log("Processing time")

    print("\nQ4:")
    x = [8, 3, 9, 5]
    sort(x)
    print(x)

    print("\nQ5:")
    print("Mean of x:", mean(x))
    print("Standard deviation of x:", std(x))

    print("\nQ6:")
    try: 
        print("A:", end=" ")
        x, y = "12.01", "2.99"  # 'Simulated' user inputs...
        x = str2intA(x)
        y = str2intA(y)
        print(x // y)
    except ZeroDivisionError as e:
        print("ZeroDivisionError​:", str(e))
    try: 
        print("B:", end=" ")
        x, y = "12.01", "2.99"  # 'Simulated' user inputs...
        x = str2intB(x)
        y = str2intB(y)
        print(x // y)
    except ZeroDivisionError as e:
        print("ZeroDivisionError​:", str(e))

    print("\nQ8:")
    print("a)", fatalStr(-1, 1))
    print("b)", fatalStr(1, -1))
    print("c)", fatalStr(0, 2))
    print("d)", fatalStr(-2, 0))

    print("\nQ9:")
    print("x = False, y = False :", exp(x = False, y = False))
    print("x = True,  y = False :", exp(x = True, y = False))
    print("x = False, y = True  :", exp(x = False, y = True))
    print("x = True,  y = True  :", exp(x = True, y = True))

    print("\nQ10:")
    print(factorial(5))