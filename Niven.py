for i in range(1,101):
  if i%(lambda x:sum([int(j) for j in list(str(x))]))(i)==0:print(i)
