def f(x):
    return (x**3) + (3*x) - 5

# Implementing False Position Method
def falsePosition(a,b,error):
    x0 = 1
    condition = True
    while condition:
        x1 = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        print("=============================")
        print('Iteration: %d \nRoot Obtained = %0.6f \nEstimate Error = %0.6f' % (x0, x1, f(x1)))

        if f(a) * f(x1) < 0:
            b = x1
            dx=b-a
        else:
            a = x1
            dx=b-a

        x0 = x0 + 1
        condition = abs(f(x1)) > error and x0<=10 and f(x1)!=0
    print("==============Finally=============")
    print('Iteration-%d \nRoot Obtained = %0.6f \nEstimate Error = %0.6f' % (x0-1, x1, f(x1)))


def check(a,b,error):
    if f(a) * f(b) > 0:
        print("Wrong numbers")
    else:
        falsePosition(a, b, error)


a = 1
b = 2
error = 0.000001
check(a,b,error)