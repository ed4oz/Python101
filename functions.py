def square(x):
    return x*x

a=square(3)
print(a)

def square(x):
    res=x*x
    return res

x=7
def f(x):
  res=5
  res*=res
  if x%2==0:
    print("Sonuc:",res)
    return res
  else:
    print("Sonuc: ",res)
  
    return res+10

print(f(4))