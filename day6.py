input = open("quiz.txt","r").read().split("\n\n")
a = "abcdefghijklmnopqrstuvwxyz"
result = 0
#6.1
for i in input:
    string = i.replace("\n","")
    for letter in a:
        if string.__contains__(letter):
            result += 1
print("6.1: " + str(result))

result = 0
#6.2

def checkForLetter(input):
    ans = a
    for letter in a:
        for answer in input:
            if not answer.__contains__(letter):
                ans = ans.replace(letter,"")
    return len(ans)
for i in input:
    string = i.split("\n")
    result += checkForLetter(string)

print("6.2: " + str(result))