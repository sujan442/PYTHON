n=int(input("enter a number:"))

def add(n):
    if(n==0 or n==1):
     return 1
    
    else:
       return n+add(n-1)
    
     
add(n)
print("the sum of the series is:",add(n))