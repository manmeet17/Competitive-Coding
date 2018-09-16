for _ in range(int(input())):
    s=input()
    stack=[]
    f=0
    for i in s:
        if i=="{" or i=='[' or i=='(':
            stack.append(i)
        else:
            if(len(stack)>0):
                t=stack.pop()
                if (i=="{" and t!="}") or (i=="[" and t!="]") or (i=="(" and t!=")"):
                    f=1
                    break
            else:
                f=1
                break
    if(f==1 or len(stack)!=0):
        print("not balanced")
    else:
        print("balanced")
