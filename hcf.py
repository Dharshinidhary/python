def calhcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if(x%i==0) and (y%i==0):
            hcf=i
    return hcf
num1=int(input("enter the number"))
num2=int(input("enter the number"))
print("H.C.F is ",calhcf(num1,num2))