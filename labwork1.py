# Ex1:
r = float(input("Enter the radius:"))
def circle_area(r):
    S = 3.14 * (r**2)
    return S
print(circle_area(r))

# Ex2:
c = float(input("Enter the temperature in Celsius?"))
F= 9/5 * c + 32
print (c,"(C) =",F,"(F)")

# Ex3:
n= int(input("enter an interger :"))
a=True if n>=2 else False
for i in range(2,n):
    if n % i == 0:
        a=False
if a:
    print("prime")
else:
    print ("not prime")

# Ex4:
n= int(input("Enter a number?"))
s=0

for i in range(1,n):
    if n % i == 0:
        s= s+ i

if s == n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
    
# Ex5:
fav = input(str("What is your favorite color?"))
colour = ["yellow", "white", "orange", "black", "purple"]
if fav in colour:
    index= colour.index(fav)
    print("Your colod is at index",index,"in my list")
else :
    print("Your colod is not in my list")
#Ex6:
range1 = range(0,7)
print([ i for i in range1])
range2 = range(1, 13, 3)
print([ i for i in range2])
range3 = range(5, 0, -1)
print([ i for i in range3])
range4 = range(6, -4, -2)
print([ i for i in range4])

# Ex7:
def remove_dollar_sign(s):
    out = ""
    for c in s:
        if c != "$":
            out = out + c
    return out
print(remove_dollar_sign("quangan$$"))

# Ex8:
def extract_even(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return result
print(extract_even([1,2,5,-1,4,10]))

# Ex9:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# Ex10:
def get_divisors(n):
    out = []
    for i in range(1, n+1):
        if n % i == 0:
            out += [i]
    return out
print(get_divisors(100))

# Ex11:
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between the points:", distance)

# Ex12:
m = int(input("Input m rows "))
n = int(input("Input n columns "))
for i in range(m):
    s = "" # for one line
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            s += "* "
        else:
            s += "  "
    print(s)