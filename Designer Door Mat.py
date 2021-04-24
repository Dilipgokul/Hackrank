n,m=map(int,input().split(" "))
lst=[]
w=".|."
for i in range(n):
    if i>0 and i< n/2 :
        pat=w.center(m,'-')
        lst.append(pat)
        print(pat)
        w=".|." + w + ".|." 
        #w=".|." *(2*i+1)   
print("WELCOME".center(m, '-'))
lst.sort(reverse=True)
print("\n".join(i for i in lst))
"""
************OR ELSE*************************
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

"""
            
    