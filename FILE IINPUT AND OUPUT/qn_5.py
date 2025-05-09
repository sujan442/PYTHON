lis=["monkey","donley","shonkey"]

with open ("qn_5.txt","r") as check:
      content=check.read()

for word in lis:
      content=content.replace(word,"#"*len(word))

with open ("qn_5.txt","w") as check:
      check.write(content)
      




# lis = ["monkey", "donley", "shonkey"]

# with open("qn_5.txt", "r") as check:
#     content = check.read()

# for word in lis:
#     content = content.replace(word, "#" * len(word))

# with open("qn_5.txt", "w") as check:
#     check.write(content)
