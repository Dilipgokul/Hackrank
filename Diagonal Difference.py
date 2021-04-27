
n=int(input())
a,b=0,0
#creates a list to store the rows,takes in the first row
lst=[list(map(int,input().split()))]

for i in range(n-1):
    lst.append(list(map(int,input().split())))
    #appends the rest of the rows
lst1=[var for i in lst for var in i]
#converting nested list into 2D list 
for i in range(0,n*n,n+1):
    a=a+lst1[i]
    #iterate left-most diagonal
for i in range(n-1,n*n-(n-1),n-1):    
    b=b+lst1[i]
    #iterate right-most diagonal,
    #take examples to find out start,stop n step
print(abs(a-b))
#abs is used to find absolute of the two

