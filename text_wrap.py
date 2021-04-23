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
        # for i in s[l:m]:
        #     if i!="$":
        #         print(i,end="")
        #     else:
        #         break
        # print("123456"+s[l:m-1])
            
            

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)
    