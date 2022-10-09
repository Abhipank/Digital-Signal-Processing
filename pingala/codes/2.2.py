import numpy as np
import matplotlib.pyplot as plt

def x(n):
 if n<0:
    return 0
 if n==0 or n==1:
    return 1
 else:
    return x(n-1)+x(n-2)

xvec=np.vectorize(x)


plt.stem(range(0,20),xvec(range(0,20)))
plt.title("Pingala Series")
plt.grid()
plt.xlabel("$n$")
plt.ylabel("$x(n)$")
plt.savefig("./figs/pingalaplot.pdf")
plt.show()