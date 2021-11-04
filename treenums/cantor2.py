from math import isqrt

def pair(x,y):
  return (x+y)*(x+y+1)//2+y

def unpair(z) :
  i=(isqrt(8*z+1)-1)//2
  x = (i * (3 + i) // 2) - z
  y = z - (i * (i + 1) // 2)
  return x,y

def ctest() :
  for n in range(42) :
    (x,y)=unpair(n)
    z=pair(x,y)
    print((x,y),'<->',z,'==',n)
    assert n==z

# rosenberg-strong pairing

def rpair(x,y) :
  m=max(x,y)
  return m*(m+1)+x-y

def runpair(z) :
  m=isqrt(z)
  q=z-m*m
  return (q,m) if q<m else (m,2*m-q)

#ctest()

def rtest() :
  for n in range(42) :
    (x,y)=runpair(n)
    z=rpair(x,y)
    print((x,y),'<->',z,'==',n)
    assert n==z

rtest()
