x=int(input("Enter A Number: "))
a=[]
def factor(x):
  print('The factors of',x,'are:')
  for i in range(1, x + 1):
    if x % i == 0:
      print(i)
      a.append(i)
factor(x)
if len(a)>2:
  print("The Number Is Composite.")
else:
  print("The Number Is Prime.")