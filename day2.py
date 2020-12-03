dat = open("passwords.txt","r").read().splitlines()
c = 0
for file in dat:
    low = int(file.split("-")[0])
    high = int(file.split("-")[1].split(" ")[0])
    letter = file.split(" ")[1].split(":")[0]
    password = file.split(" ")[2]
    print(file)
    if (password[low-1] == letter and not password[high-1] == letter) or (password[high-1] == letter and not password[low-1] == letter):
        c += 1

print(c)