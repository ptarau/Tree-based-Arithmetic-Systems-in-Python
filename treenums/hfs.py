# hereditarily finite sets

class hfs(frozenset):
  def __new__(cls, *args):
    return frozenset.__new__(cls,args)
    
  def __repr__(self) :
    s=super().__repr__()
    if s=="hfs()" : return "{}"
    return s[4:-1]

# examples

empty=hfs()

one = hfs(empty)

two=hfs(empty,one)

print('empty:',empty)
print('one:',one)
print('two:',two)

def nat() :
  n=0
  while True:
    yield n
    n+=1

def take(k,gen) :
  for x in gen:
    if k<=0 : break
    yield x
    k-=1

print(hfs(*take(5,nat())))

'''
# output:

empty: {}
one: {{}}
two: {{}, {{}}}
{0, 1, 2, 3, 4}
'''