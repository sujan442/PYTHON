# with open("qn_7.txt","r") as f:
#     content=f.readline()

#     lineno=1

# for line in content:
#      if("Python" in content):
#        print(f"Python is present.line no:{line}")
#        break
#      lineno+=1
# else:
#        print("python is not present:")


with open("qn_7.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")