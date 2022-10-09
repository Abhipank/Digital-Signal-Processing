import numpy as np
import matplotlib.pyplot as plt

def x(n):
 if n<0:
    return 0
 if n==0 or n==1:
    return 1
 else:
    return x(n-1)+x(n-2)


def y(n):
 return x(n+1)+x(n-1)

xvec=np.vectorize(x)
yvec=np.vectorize(y)

plt.stem(range(0,20),yvec(range(0,20)))
plt.ylabel("$y(n)$")
plt.xlabel("$n$")
plt.grid()

plt.savefig("./figs/yplot.pdf")
plt.show()