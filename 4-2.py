inputData = input().split()

buff = []

for i in inputData:
    try:
        if(type(int(i)) == int):
            buff.append(int(i))

    except:
        right = buff.pop()
        left = buff.pop()

        if(i == '+'):
            buff.append(left+right)
        
        elif(i == '-'):
            buff.append(left-right)

        elif(i == '*'):
            buff.append(left*right)


print(buff.pop())
