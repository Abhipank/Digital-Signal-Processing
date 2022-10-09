import numpy as np

al=(1+np.sqrt(5))/2
be=(1-np.sqrt(5))/2

def a(n):
    if n<1:
        return 0
    else:
        return (al**n-be**n)/(al-be)

def b(n):
    return a(n-1)+a(n+1)

avec=np.vectorize(a)
N=50
collec=np.arange(1,N)
ep=1e-3


if(abs(sum(avec(collec))-a(N+1)+1)<ep):
 print("1st option Correct")
else:
 print("1st option Incorrect")

collec=np.arange(1,100)
def aten(n):
    return avec(n)/10**n

atenv=np.vectorize(aten)


if(abs(sum(atenv(collec))-10/89)<ep):
 print("2nd option Correct")
else:
 print("2nd option Incorrect")

if(abs(b(N)-(al**N+be**N))<ep):
 print("3rd option Correct")
else:
 print("3rd option Incorrect")

def bten(n):
    return b(n)/10**n

btenv=np.vectorize(bten)

if(abs(sum(btenv(collec))-8/89)<ep):
 print("4th option Correct")
else:
 print("4th option Incorrect")
