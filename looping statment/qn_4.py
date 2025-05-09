a=int(input("enter any number:"))
for i in range (2,a):
    if(a%i)==0:
        print("number is composite:")
        break

else:
    print("number is prime:")