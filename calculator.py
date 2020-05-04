
def calculator(a):
    stack=[]
    a = a.split(" ")
    for s in a:
        if s.isnumeric():
            stack.append(int(s))
            print(stack)
        else:
            if(len(stack)==1):
                stack.append(s)
            else:
                x=op_prec(stack[len(stack)-2],s)
                if(x==0): stack.append(s)
                elif(x==-1 or x==1):
                    while(1):
                        if(len(stack)==1): break
                        elif(op_prec(stack[len(stack)-2],s)!=0):
                            operand2=pop_stack(stack)
                            operator=pop_stack(stack)
                            operand1=pop_stack(stack)
                            if(operand2==0 and operator=="/"): return "invalid"
                            stack.append(operate(operand1,operator,operand2))
                        else: break
                        #print(stack)
                    stack.append(s)


    while(len(stack)!=1):
        operand2=pop_stack(stack)
        operator=pop_stack(stack)
        operand1=pop_stack(stack)
        if(operand2==0 and operator=="/"): return "invalid"
        stack.append(operate(operand1,operator,operand2))
    return stack[0]
#print(stack)
def pop_stack(stack):
    x=stack.pop(len(stack)-1)
    return x


def operate(operand1,operator,operand2):
    if(operator=="+"): return operand1+operand2
    elif(operator=="-"): return operand1-operand2
    elif(operator=="*"): return operand1*operand2
    else: return operand1//operand2

def op_prec(x,y):
    if (x=="/" or x=="*") and (y=="+" or y=="-"):
        return 1
    elif (x=="+" or x=="-") and (y=="/" or y=="*"):
        return 0
    else:
        return -1

