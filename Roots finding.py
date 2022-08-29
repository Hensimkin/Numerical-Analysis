import math

import sympy as sp
from sympy.utilities.lambdify import lambdify

def polynom(x):
    return (x**4)+(x**3)-(3*(x**2))


def Bisection_Method(polynom,start_point,end_point,eps):
    z=polynom
    bigarray=[]
    size=(abs(start_point)+abs(end_point))/0.1
    num=start_point
    for i in range(int(size)+1):
        smallarray = []
        smallarray.append(num)
        smallarray.append(round(polynom(num),4))
        bigarray.append(smallarray)
        num = num + 0.1
        num=round(num,3)

    for i in range(1,int(size),1):
        if (bigarray[i][1]*bigarray[i-1][1])<0:
            print("I", "   ", "A", "   ", "B", "   ", "C", "   ", "F(a)", "   ", "F(b)", "   ", "F(c)")
            Bisection(polynom, bigarray[i-1][0], bigarray[i][0], eps)
    x = sp.symbols('x')
    f2 = diff(polynom)
    f3 = lambdify(x, f2)
    for i in range(int(size)+1):
        num=round(bigarray[i][0],6)
        f4=round(f3(num),6)
        bigarray[i].append(f4)

    for i in range(1, int(size)+1, 1):
        if (bigarray[i][2] * bigarray[i - 1][2]) < 0:
            print("I", "   ", "A", "   ", "B", "   ", "C", "   ", "F'(a)", "   ", "F'(b)", "   ", "F'(c)")
            Bisection(f3, bigarray[i - 1][0], bigarray[i][0], eps)


def diff(polynom):
    x = sp.symbols('x')
    my_f = polynom(x)
    return sp.diff(my_f, x)




def Bisection(polynom,a,b,eps):
    c=0
    fc=0
    i=1
    counter=0
    temp=0
    while(abs(a-b) >eps):
        c=round((a+b)/2,6)
        fc=round(polynom(c),6)
        if fc<0 and polynom(a)<0:
            temp=round(a,6)
            counter=1
            a=c
            a=round(a,6)
        if fc<0 and polynom(b)<0:
            temp=round(b,6)
            counter=2
            b=c
            b = round(b, 6)
        if fc>0 and polynom(a)>0:
            temp=round(a,6)
            counter=1
            a=c
            a = round(a, 6)
        if fc>0 and polynom(b)>0:
            temp = round(b, 6)
            counter=2
            b=c
            b = round(b, 6)
        if counter==1:
            print(i, " ", temp, " ", b, " ", c, " ", round(polynom(temp),6), " ", round(polynom(b),6), " ", round(fc,6))
        if counter==2:
            print(i, " ", a, " ", temp, " ", c, " ", round(polynom(a),6), " ", round(polynom(temp),6), " ", round(fc,6))
        i+=1
    print("The point is: ",c)




def Newton_Raphson(f,start,end,eps):
    x = sp.symbols('x')
    f_prime=diff(f)
    f_prime = lambdify(x, f_prime)
    xr=round((start+end)/2,6)
    result1=round(f(xr),6)
    result2=round(f_prime(xr),6)
    i=1
    print("f'(x)         f(x)         xr      iteration num     ")
    print(result2,"      ",result1,"      ",xr,"      ",i,"     x0=",xr)
    xr_next=round(xr-(result1/result2),6)
    while(abs(xr-xr_next)>eps):
        i+=1
        xr=round(xr_next,6)
        result1 = round(f(xr),6)
        result2 = round(f_prime(xr),6)
        xr_next = round(xr - (result1 / result2),6)
        print(result2, "      ", result1, "      ", xr, "      ", i)
    print("the result of the function in that range is: ",xr_next)


def secent_method(py,start,eps):
    f=py
    x0=start
    x1=start+1
    result1=round(f(x0),6)
    result2=round(f(x1),6)
    i=0
    print("i      xi       xi+1       f(xi)        f(xi+1)")
    print(i,"     ",x0,"      ",x1,"      ",result1,"      ",result2)
    x2=round((x0*result2-x1*result1)/(result2-result1),6)
    while(abs(x2-x1)>eps):
        i+=1
        x0=round(x1,6)
        x1=round(x2,6)
        result1=round(result2,6)
        result2=round(f(x1),6)
        x2 = round((x0 * result2 - x1 * result1) / (result2 - result1),6)
        print(i, "     ", x0, "      ", x1, "      ", result1, "      ", result2)
    print("the result of the function in that range is: ", x2)




def main():
    f = lambda x: (x ** 4) + (x ** 3) - (3 * (x ** 2))
    start=-3
    end=2
    eps=0.0001
    flag=True
    while flag:
        a=int(input("please select method\n1.bisection\n2.Newton Raphson\n3.secent\n4.exit"))
        if a==1:
            Bisection_Method(f,start,end,eps)
        if a==2:
            Newton_Raphson(f,start,end,eps)
        if a==3:
            secent_method(f,start,eps)
        if a==4:
            flag=False




#Bisection_Method(polynom,-3,2,0.0001)
#f=lambda x:(x**4)+(x**3)-(3*(x**2))
#f=lambda x:(4*x**3)-(48*x)+5
#Newton_Raphson(f,-3,2,0.0001)
#Newton_Raphson(f,3,4,0.001)
f=lambda x:(x**3)-math.cos(x)
#secent_method(f,0,0.001)
main()


