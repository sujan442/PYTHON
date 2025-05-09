a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
def greatest():
    if(a>b and a>c):
        print(f"the greatest number is{a}")

    elif(b>a and b>c):
        print(f"the greatest number is{b}")

    elif(c>a and a>c):
        print(f"the greatest number is{c}")

    else:
        print("wrong input:") 
       
    return "ok"

q=greatest()
print(q)

