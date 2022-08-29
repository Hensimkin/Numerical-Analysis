import math
import sympy
import sympy as sp
from sympy import solve, Eq
from sympy.utilities.lambdify import lambdify
def derive(f):
    x = sp.symbols('x')
    f_prime = f.diff(x)
    #y = lambdify(x, f)
    #f_prime = lambdify(x, f_prime)
    return f_prime



def findanswer(f):
    z=solve(f)
    return z


def numofparts(func,originalfunc,points):
    arr=[]
    x = sp.symbols('x')
    func = lambdify(x, func)
    for i in range(len(points)):
        if func(points[i])<0:
            arr.append(points[i])
    originalfunc = lambdify(x, originalfunc)
    max=originalfunc(points[0])
    for i in range(len(arr)):
        if originalfunc(points[i])>max:
            max=originalfunc(points[i])
    print(max)
    return max




def findingn(a,b,max,error):
    m=((((b-a)**3)*max)/error)/12
    m=int(math.sqrt(m))
    return m


def total(a,b,h,func):
    x = sp.symbols('x')
    func = lambdify(x, func)
    z=a
    y=a+h
    total=0
    while z<b:
        total=total+(0.5*(y-z)*(func(z)+func(y)))
        z=z+h
        y=y+h
    print(total)


def main1():
    error = 0.000002
    a = 0
    b = math.pi
    x = sp.symbols('x')
    y = sp.sin(x)
    func = derive(y)
    findanswer(func)
    func2 = derive(func)
    z = numofparts(func2, y, findanswer(func))
    n = findingn(0, math.pi, z, error)
    h = (b - a) / n
    total(a, b, h, y)




def simpson(table,n):
    h=(table[len(table)-1][0]-table[0][0])/n
    total=table[0][1]
    for i in range(1,len(table)-1):
        if i%2==0:
            total = total + (2*table[i][1])
        else:
            total = total + (4 * table[i][1])
    total=total+ table[len(table)-1][1]
    return (1/3)*h*total




def calculateder4(func,a,b):
    z=func
    z=derive(z)#1
    arr=solve(z)
    for i in range(3):
        z=derive(z)#4
    max=numofparts(func, z, arr)
    x = sp.symbols('x')
    func = lambdify(x, func)
    return func(max)


def calcall(h,n,a,b,max):
    #total=((h**5)/90)*((b-a)/h)*(max/2)
    total=((1/180)*(h**4))*(b-a)*max
    print(total)


def main2():
    table = [[0, 0], [math.pi / 4, 0.70710], [math.pi / 2, 1], [(3 * math.pi) / 4, 0.70710], [math.pi, 0]]
    n = 4
    h = (table[len(table) - 1][0] - table[0][0]) / n
    print(simpson(table, n))
    x = sp.symbols('x')
    func = sp.sin(x)
    max = calculateder4(func, table[0][0], table[len(table) - 1][1])
    calcall(h, n, table[0][0], table[len(table) - 1][0], max)



main1()
main2()






