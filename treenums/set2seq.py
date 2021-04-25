from hfs import take
import random

def seq2mset(xs) :

  def loop():
    s=0
    for x in xs:
      s+=x
      yield s
  return list(loop())

def mset2seq(ms) :
  def loop() :
    s=0
    for m in ms :
      yield m-s
      s=m
  return list(loop())

def seq2set(xs) :
  def loop():
    s = -1
    for x in xs:
      sx=x+1
      s+=sx
      yield s
  return list(loop())

def set2seq(ms) :
  def loop() :
    s=0
    for m in ms :
      yield m-s
      s=m+1
  return list(loop())


def set_derivatives(s) :
  d=sorted(set(s))
  while any(d):
    yield d
    d=sorted(set(set2seq(d)))
  yield d

def mset_derivatives(s) :
  d=sorted(s)
  while any(d[0:-1]) and d[-1]!=1:
    yield d
    d=sorted(mset2seq(d))
  yield d


def dtest(n=1000,k=20):
  s=set(random.sample(range(n), k))
  print('-' * 10)
  for x in take(10,set_derivatives(s)):
    print(x)
  print('-'*10)

#dtest()

def mtest(n=1000,k=32):
  s=set(random.sample(range(n), k))
  print('-' * 10)
  for x in take(36,mset_derivatives(s)):
    print(x)
  print('-'*10)

mtest()

def set2bin(xs,l=None) :
  if not l : l = xs[-1]+1
  bs=[0]*l
  for i in xs:
    bs[i]=1
  return bs

def bin2set(bs) :
  return [i for (i,b) in enumerate(bs)
       if b == 1]

# tests

def seqop(f,a,b) :
  x = set(seq2set(a))
  y = set(seq2set(b))
  z = f(x,y)
  c=set2seq(z)
  return c

def seqint(a,b) :
  return seqop(lambda x,y : x.intersection(y),a,b)

def t1() :
  a=[0,9,0,1,3,0,2,5,7,2,0,0]
  b= seq2set(a)
  c=set2seq(b)
  bs=set2bin(b,50)
  print('b',b)
  print(bs)
  d=bin2set(bs)
  print('d',d)

def t2() :
  a= (9,0,3,3,1,0,4,0,2,7,0,2,5,5)
  b= (0,1,0,4,5,5,2,0,9,0,2,1,1)
  c=seqint(a,b)
  return c

if __name__ == "__main__" :
  print(t2())
  pass

