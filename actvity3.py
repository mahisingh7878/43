#write a program to create a list with five student 'details (rool no , name,grade ,school).
#Then convert that list into a dictionary.

def convertTodict(lst):
    mydict={}
    for iteam in lst:
        mydict[iteam[0]]=iteam[1:]
    return mydict

students=[[1,'Ali',1],[2,'ayat',1],[3,'mahi',3]]

print("List is ",students)
print("converted dictionary is ",convertTodict(students))
        

