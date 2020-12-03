dat = open("dates.txt","r").read().splitlines()

for file in dat:
    for add in dat:
        for third in dat:
            if int(file) + int(add) + int(third)== 2020:
                print(int(file)*int(add)*int(third))



