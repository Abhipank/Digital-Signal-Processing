import numpy as np
import matplotlib.pyplot as plt


al=(1+np.sqrt(5))/2
be=(1-np.sqrt(5))/2

def a(n):
    if n<1:
        return 0
    else:
        return (al**n-be**n)/(al-be)



b=np.zeros(500)

def b(n):
    return a(n-1)+a(n+1)


def bten(n):
    return b(n)/10**n


btenv=np.vectorize(bten)



def func(k):
    return sum(btenv(range(1,k+1)))


coll=np.arange(1,101)
sumv=np.vectorize(func)




plt.stem(coll,sumv(coll))
plt.grid()
plt.xlabel("$k$")
plt.ylabel("$\sum b_k/10^{k}$")
plt.axhline(y=8/89,color='g')
plt.legend(["y=8/89","$\sum b_k/10^{k}$"],loc='upper right')
plt.savefig("./figs/proof1.4.pdf")
plt.show()