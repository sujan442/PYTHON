with open("poem.txt") as check:
    content=check.read()

    print(content)

if ("twinkle" in content):
    print("it contains:")

else:
    print("It doesn't contain:") 