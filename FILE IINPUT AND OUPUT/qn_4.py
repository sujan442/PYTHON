word="Donkey"

with open("qn_4.txt","r") as content:
   new=content.read()

new_content=new.replace("Donkey","####")  

with open ("qn_4.txt","w") as content:
          content.write(new_content)