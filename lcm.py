def find_lcm(x,y):

    if(x>y):
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("The L.C.M. is",find_lcm(a, b))