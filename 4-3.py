from collections import deque

inputData = input().split()

processNum = int(inputData[0])
q = int(inputData[1])
schedule = deque([])


for i in range(processNum):
    inputBuff = input().split()
    schedule.append([inputBuff[0],inputBuff[1]])

time = 0

while len(schedule) != 0:
    buffData = schedule.popleft()
    buffTime = int(buffData[1])

    if buffTime>100:
        schedule.append([buffData[0],buffTime-100])
        time += 100

    else:
        time += buffTime
        print(buffData[0],"  ",time)
