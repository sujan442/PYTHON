sets={23,34,56,"sujan"}
print(sets)
sets.add("pujan")
print(sets)
sets.remove("sujan")   #remove sujan from the setss
print(sets)
sets.pop()
print(sets)
sets.clear()
print(sets)
a=(sets.union({34,57}))
print(a)   #Remember that union() and intersection() methods return new sets rather than modifying the original set in place 
b=sets.intersection({34,57,34})
print(b)   #Remember that union() and intersection() methods return new sets rather than modifying the original set in place 