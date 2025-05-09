marks={
    "sujan":100,
    "pujan":70,
    "lujan":60

}
print(marks, type(marks))
a=marks.items()
print(a)
print(marks.keys())
print(marks.get("sujan"))
marks.update({"sujan":50})
print(marks)
