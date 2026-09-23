for i in range (1,101,1):
    print(i)
    if(i==10):
       break
else:
   print("task complited")
   print("Done with that task")

#Calculate Compound Interest
p=10000
r=10
t=2
compound_intrest=p*((1+r/100)*(1+r/100))
print(compound_intrest)
# output=12100.000000000002