#program to find greatest among four numbers

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))
if(a>b and a>c and a>d):
    print("the greatest is A")


if(b>a and b>c and b >d):
    print("the greatest is B")
      

if(c>a and c>b and c>d):
    print("the greatest is C")