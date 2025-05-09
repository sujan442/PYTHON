# def generateTable(n):
#     table=""
#     for i in range (1,11):
#        table+=f"{n}*{i}:{n*i}\n"


#     with open(f"table/table_{n}.txt","w") as mul:
#         mul.write(table)

    
    
# for i in range(2,21):
#         generateTable(i)        



def table(n):
        tab=""
        for i in range(1,11):
            tab+=f"{n}*{i}:{n*i}\n"

        with open(f"product/product_{n}.txt","w") as mul:
               mul.write(tab)


for i in range (2,21):
    table(i)        


