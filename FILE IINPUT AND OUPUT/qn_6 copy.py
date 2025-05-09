with open("qn_6.txt","r") as f:
    content=f.readline()

    lineno=1

for line in content:
     if("Python" in content):
       print(f"Python is present.line no:{line}")
       break
     lineno+=1
else:
       print("python is not present:")