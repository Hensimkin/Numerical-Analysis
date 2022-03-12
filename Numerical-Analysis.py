
import numpy as np
print(np.finfo(float).eps)
print(np.finfo(np.float32).eps)
"""""
The first functions represents the differnce between floating point as machine prescion
"""""

def maachineEpsilon(eps):
    while(1+eps)!=1:
        prev_eps=eps
        eps = eps / 2
    print("machine epsilon is:",prev_eps)

maachineEpsilon(0.5)

print(abs(3.0*(4.0/3.0-1)-1))

print(round(abs(3.0*(4.0/3.0-1)-1)))
