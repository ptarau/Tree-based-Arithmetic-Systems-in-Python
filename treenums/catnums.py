# computing with binary trees (with empty leaves)
 
import visuals

# bijection from N to T (standing for the set of binary trees)
def t(n) :
  if n==0 : return ()
  else :
    assert n>0
    x,y = to_pair_with(nparity(n),n)
    ys = t(y)
    if x==0 :
      zs=ys
    else :
      return  t(x-1),ys

# inverse of t, from trees to N
def n(t) :
 if t==() : return 0
 else :
   x,xs=t
   b = tparity(t)
   if b==0 : return 2**(n(x)+1)*n(xs)
   else : return 2**(n(x)+1)*(n(xs)+1)-1

# parity, in N 
def nparity(n) : return n % 2

# split into count of 0s/1s ending it and the rest of a number  
def to_pair_with(b,z) :
  x=0
  while z>0 and nparity(z)==b :
    z=(z-b)//2
    x+=1
  return x,z
    
# parity in T
def tparity(xs) :
  l=0
  while xs :
    x,ys=xs 
    xs=ys 
    l+=1 
  return l%2

# successor, from T to T without empty tree  
def s(t) :
  one = (),()
  if t==() : return one
  else :
    x,y=t
    if y==() : return x,one
    else :
      u,v=y
      b=tparity(t)
      if b == 0 :
        if x == () : return s(u),v
        else : 
          return (),(s_(x),y)      
      else :
        if u == () and v != ():
          w,z=v
          return x,(s(w),z)
        else :
          return x, ((),(s_(u),v))

# predecessor, from T without empty tree  to T         
def s_(t) :
  one = (),()
  x,y=t
  if t == one : return ()
  elif y == one : return x,()
  else :
    b=tparity(t)
    if b == 0 :
      u,v=y
      if u == () and v != () :
        w,z=v
        return x,(s(w),z)
      else :
        return x, ((),(s_(u),v))     
    else :
      if x == () :
        u,v=y
        return s(u),v
      else :
        return (),(s_(x),y)

# double, from T to T     
def db(t) :
  if t == () : return ()
  else : 
    if tparity(t) == 0 :
      x,y=t
      return s(x),y
    else :
      return (),t

# half rounded down, from T to T  
def hf(t) :
  if t == () : return ()
  else :
    x,y=t
    if x == () : return y
    else : return s_(x),y  

# power of 2, from T to powers of 2 in T
def exp2(t) :
  one = (),()
  if t == () : return one
  else : return s_(t),one

# integer log of 2, from powers of 2 in T, to T
def log2(t) :
  one = (),()
  if t == one : return ()
  else :
    x,y=t
    assert y==one
    return s(x)
  
# tests

def t1() :
  for x in range(10000) :
    y=n(s_(s(t(x))))
    if x != y : print(x,y) 
  for x in range(1,10000) :
    y=n(s(s_(t(x))))
    if x != y : print(x,y) 
  print('done')
  
  
def t2() :
  for x in range(10000) :
    y=n(hf(db(t(x))))
    if x != y : print(x,y) 
  for x in range(0,10000,2) :
    y=n(db(hf(t(x))))
    if x != y : print(x,y) 
  print('done')
  

# visuals

# draw n as a tree
def st(n) :
  tnum=t(n)
  dt=decorate(tnum)
  visuals.showTree(dt)

# draw n as a digraph
def sd(n) :
  tnum=t(n)
  dt=decorate(tnum)
  visuals.showDag(dt) 
  
def decorate(t) :
    if t == () : return ('0',)
    else :
      x,y=t
      return (str(n(t)),decorate(x),decorate(y))  
  
'''
def cons(triplet) : 
  b,i,j = triplet
  return 2^(i+1)*(j+b)-b

def nn(t) :
  b = parity(t)
  def f(b,t) :
    if t==() : return 0
    else :
      x,y=t
      return cons(b,nn(x),f(1-b,y))
    
  
  
def decons(k) :
  assert k>0
  b = nparity(k)
  i,j = dval(k+b)
  if i==0 :
    i0 = 0
  else :
    i0 = i-1
  return b,i0,j-b

def dval(z) :
  x=0
  while z>0 and nparity(z)==0 :
    z=z//2
    x+=1
  return (x,z)  
''' 
  
  
