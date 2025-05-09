n=int(input("enter any number:"))
def cm(inches):
    return inches * 2.54

print(f"after conversion:{cm(n)}")



# Even though the input variable is called n and the function parameter is called inches, there's no error because:

# You're passing n as an argument to the function:

# cm(n)
# Inside the function, n is passed to the parameter inches. So now, inches = n, and the function uses that value correctly.