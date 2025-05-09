# a=int(input("enter a number:"))
# for i in range(1,11,-1):
#     print(f"{a}*{i} : {a*i}")
a = int(input("enter a number: "))

for i in range(10,0,-1):  # Start at 10, end before 0, step -1
    print(f"{a} * {i} = {a * i}")
