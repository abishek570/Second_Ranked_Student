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

##Removing the last element (Which is 1st Ranked)
b=l3.pop()

##Last number which is second Now. Checking whether it is ranked by another person
i=len(l3)-1
while i>=0:
    if b[1]==l3[i][1]:
        l3.pop()
    else:
        break
    i-=1

##Storing the second ranked Students in a list - l4 
l4=[]
l4.append(l3[-1])
b=l3[-1][1]
i=len(l3)-2
while i>=0:
    if b==l3[i][1]:
        l4.append(l3[i])
    i-=1

## Sorting them based on Names, and print only the names
l5=sorted(l4)
for i,j in l5:
    print(f"{i} scored second rank by scoring {j} Marks.")



