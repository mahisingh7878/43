dict1={'Name':'Ali','grade':1}

print(dict1)

dict1["age"]=12

print("updated dictionary after adding",dict1)

print("Name of student ",dict1.get('Name'),"and grade is ",dict1.get('grade '))

dict1.pop('grade')

print("Dictionary after removal is ",dict1)
