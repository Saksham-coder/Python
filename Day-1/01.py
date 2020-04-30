def left(a):
  aleft = 1
  for i in a:
    aleft *= i
  return aleft

def right(b):
  bright = 1
  for i in b:
    bright *= i
  return bright

arr=[1,2,3,4,5]
newarr=[]
for i in range(len(arr)):
  a,b = (left(arr[:i]), right(arr[i+1:]))
  newarr.append(a*b)
print(newarr)