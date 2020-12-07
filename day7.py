
input = open("bags","r").read().splitlines()
#input = open("testbags.txt","r").read().splitlines()

#7.1
bags = []
for i in input:
    if i.split("contain")[1].__contains__("shiny gold"):
        bags.append(i.split(" contain")[0])
for color in bags:
    for i in input:
        if i.split("contain")[1].__contains__(color[:-1]):
            if not bags.__contains__(i.split(" contain")[0]):
                bags.append(i.split(" contain")[0])
print("7.1: " + str(len(bags)))

#7.2

counter = 0
def recur(color,amount):
    global counter
    for i in input:
        i = i.replace("s","").replace(".","")
        if i.split(" contain ")[0].__contains__(color):
            for b in i.split(" contain ")[1].split(", "):
                if not b.__contains__("no"):
                    print("From: " + str(color), "Amount: " + str(int(b[:2])*int(amount)), "Color: " + b[2:])
                    counter += (int(b[:2]) * int(amount))
                    recur(b[2:],int(b[:2])*int(amount))
    return counter

print("Bags needed: " + str(recur("hiny gold",1)))
