input = open("day8input.txt", "r").read().splitlines()

visited = []
nopA = []
jmpA = []
value = 0

def getAllNopAndJump():
    global nopA
    i = 0
    while i < len(input):
        if input[i][:3] == "nop":
            nopA.append(i)
        elif input[i][:3] == "jmp":
            jmpA.append(i)
        i += 1

def changeNopToJump():
    global nopA
    global jmpA
    visited = []
    broke = False
    for n in nopA:
        input[n] = "jmp "+input[n][4:]
        i = 0
        value = 0
        visited = []
        while i < len(input):
            if visited.__contains__(i):
                visited = []
                broke = True
                break
            else:
                visited.append(i)
                if input[i][:3] == "acc":
                    value += int(input[i][4:])
                    i += 1
                elif input[i][:3] == "nop":
                    i += 1
                elif input[i][:3] == "jmp":
                    i += int(input[i][4:])
        if broke:
            broke = False
        else:
            print("Error found in Line: " + str(i) + "! Right Value is: " + str(value))
        input[n] = "nop " + input[n][4:]

def changeJumpToNop():
    global nopA
    global jmpA
    visited = []
    for n in jmpA:
        input[n] = "nop "+input[n][4:]
        i = 0
        value = 0
        visited = []
        while i < len(input):
            if visited.__contains__(i):
                visited = []
                broke = True
                break
            else:
                visited.append(i)
                if input[i][:3] == "acc":
                    value += int(input[i][4:])
                    i += 1
                elif input[i][:3] == "nop":
                    i += 1
                elif input[i][:3] == "jmp":
                    i += int(input[i][4:])
        if broke:
            broke = False
        else:
            print("Error found in Line: " + str(i) + "! Right Value is: " + str(value))
        input[n] = "jmp " + input[n][4:]

def TaskOne():
    value = 0
    i = 0
    visited = []
    while i < len(input):
        if visited.__contains__(i):
            break
        else:
            visited.append(i)
            if input[i][:3] == "acc":
                value += int(input[i][4:])
                i += 1
            elif input[i][:3] == "nop":
                i += 1
            elif input[i][:3] == "jmp":
                i += int(input[i][4:])
    print("Value for Task One with Bug included, when the loop is reentered: " + str(value))

def TaskTwo():
    getAllNopAndJump()
    changeNopToJump()
    changeJumpToNop()


TaskOne()
TaskTwo()