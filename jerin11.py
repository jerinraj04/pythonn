def power(base):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("enter exponential value: "))
print("result:",power(base,exp))
