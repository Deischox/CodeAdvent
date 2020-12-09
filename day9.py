input = open("day9input.txt","r").read().splitlines()
input = [ int(x) for x in input ]


def getLastTwe(input,i):
    l = []
    c = 25
    while c > 0:
        l.append(input[i-c])
        c -= 1
    return l

def checkValue(array,v):
    checked = False
    for i in array:
        for l in array:
            if l != i:
                if int(i)+int(l) == int(v):
                    checked = True
    return checked


def findRow(array,value,index):
    i = 0
    maxx = int(index)
    while maxx > 1:
        while i < maxx:
            if sum(input[i:maxx]) == value and len(input[i:maxx]) > 1:
                print("Found")
                print(input[i:maxx])
                print("Code: ",min(input[i:maxx])+max(input[i:maxx]))
            i += 1
        i = 0
        maxx -= 1


i = 25
value = 0
index = 0
while i < len(input):
    if not checkValue(getLastTwe(input, i), input[i]):
        value = input[i]
        index = i
        print(input[i],i)
    i += 1

findRow(input,value,index)