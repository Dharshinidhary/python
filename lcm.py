def lcmval(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while(1):
        if(greater % x == 0)and (greater % y == 0 ):
            lcm=greater
            break
        greater += 1
    return lcm
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
print("The L.C.M is ",lcmval(num1,num2))
