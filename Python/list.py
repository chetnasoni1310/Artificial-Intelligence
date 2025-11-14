marks = [1,2,3]



print( marks[0])
print( marks[-1])
print( marks[1:3])



marks.append(45)
marks.insert(0,234)



for item in marks :
    print(item)



print( len(marks))    




i = 0
while i<len(marks):
    print(marks[i])
    i+=1
  


marks.clear()  
print( marks )