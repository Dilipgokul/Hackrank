# print(chr(97))
"""
n = int(input())
if n>1:
    pattern=[(chr(97)).center(n, '-')]
    
for i in range(1,n+1):
    # pat =("-"+chr(97+1*i)+"-"+chr(97)+"-"+chr(97+1*i)).center(n, '-')
    pat =(chr(97)).center(n, '-')
    
    pattern.append(("-"+chr(97+1*i)+pat+chr(97+1*i)).center(n, '-'))
print('\n'.join(pattern + ['WELCOME'.center(n, '-')] + pattern[::-1]))

# pattern = [(chr(97+1*i)).center(n, '-') for i in range(n)]
# print('\n'.join(pattern + ['WELCOME'.center(n, '-')] + pattern[::-1]))


****************************************
def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)
           
import string
N = int(input())
alphabet = string.ascii_lowercase

for i in range(N-1, -N, -1):
    row = ["-"]*(4*N-3)

    for j in range(0, N - abs(i)):
        row[2*(N-1+j)] = alphabet[abs(i)+j]
        row[2*(N-1-j)] = alphabet[abs(i)+j]
    print("".join(row))
    """
# import string

# size = int(input())
# alphabet = string.ascii_lowercase

# for i in range(size - 1, 0, -1):
#     row = ["-"] * (size * 2 - 1)
#     for j in range(0, size - i):
#         row[size - 1 - j] = alphabet[j + i]
#         row[size - 1 + j] = alphabet[j + i]
#     print("-".join(row))

# for i in range(0, size):
#     row = ["-"] * (size * 2 - 1)
#     for j in range(0, size - i):
#         row[size - 1 - j] = alphabet[j + i]
#         row[size - 1 + j] = alphabet[j + i]
#     print("-".join(row))
   

def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))