a=int(input("enter marks:"))
b=int(input("enter marks:"))
c=int(input("enter marks:"))
# if(a>33 and b>33 and c>33):
#     print("good marks")                 #commented program is wrong according question
# else:
#     print("bad marks:")
marks=(a+b+c)/3
print(marks)
if (marks>40 and a>33 and b>33 and c>33 ):
    print("stydent is pass:")
else:
    print("student is fail:")