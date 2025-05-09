# # finding factorial
n=int(input("enter any number:"))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*fact(n-1))
    
print(f"the factorial of n is:{fact(n)}")


# n=int(input("enter any number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i

# print(f"the factorial is:{fact}")