import sys

while(True):
        st = sys.stdin.readlines()
        if(st):
                st = str(st)
                for i in range(len(st)-1):
                        if(st[i]=='/' and st[i+1]=='/'):
                                break
                        elif(st[i]=='-' and st[i+1]=='>'):
                                st = st[:i]+'.'+st[i+2:len(st)]
                print(st)
        else:
                break
