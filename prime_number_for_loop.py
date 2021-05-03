prime_list=[]

for i in range (1,100):
  if i>1:
    for j in range (2,i):
      if i % j == 0:
         break
    else:
      prime_list.append(i)    
       
print(prime_list)