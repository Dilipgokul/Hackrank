import textwrap

def wrap(string, max_width):
        l=0
        m=max_width
        p=int((len(string))/max_width)
        s=string+"$"
        for i in range(p+1):
            last=s.find('$')
            if "$" not in s[l:m]:
                print(s[l:m])
                l+=max_width
                m+=max_width
            else:
                print(s[l:last])
        
            
            

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)

'''
this is the alternative
def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    '''