##Second highest Student finder in ordered list based on grades:

l1=[]

##Getting inputs - Name, Score
for _ in range(int(input())):
    name = input()
    score = float(input())
    l1.append([name,score])
    
##Sorting the list based on Grades
def sorting(l2:list)-> list:
    i=0
    j=1
    while i<(len(l2)-1):
        if l2[i][j]>l2[i+1][j]:
            temp=l2[i]
            l2[i]=l2[i+1]
            l2[i+1]=temp
            if l2[i+1][j]<l2[i][j]:
                temp1=l2[i+1]
                l2[i]=l2[i+1]
                l2[i]=temp1
            else:
                pass
        else:
            pass
        i+=1
    return l2

for i in range(len(l1)):
    l3=sorting(l1)

##Removing the first element (Which is last Rank)
b=l3.pop(0)

i=0
while i<len(l3):
    if b[1]==l3[0][1]:
        l3.pop(0)
    i+=1
##Getting all the second lowest grades in list - l4
l4=[]
b=l3[0][1]
i=0
while i<len(l3):
    if b==l3[i][1]:
        l4.append(l3[i])
    else:
        pass
    i+=1

print(l4)
l5=sorted(l4)
for i,j in l5:
    print(f"{i} scored the second lowest score of {j} Marks.")





