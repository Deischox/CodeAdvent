statements = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

data = open("passport.txt","r").read().splitlines()
valid = 0
points = []

passport = ""
#Is missing the last pasport
for i in data:
    if len(i) == 0 or data[-1] == i:
        if passport.__contains__("byr"):
            if int(passport.split("byr:")[1][0:4]) <= 2002 and int(passport.split("byr:")[1][0:4]) >= 1920:
                #print("byr: " + passport.split("byr:")[1][0:4] + " A ")
                if passport.__contains__("iyr"):
                    if int(passport.split("iyr:")[1][0:4]) <= 2020 and int(passport.split("iyr:")[1][0:4]) >= 2010:
                        #print("iyr: " + passport.split("iyr:")[1][0:4] + " A ")
                        if passport.__contains__("eyr"):
                            if int(passport.split("eyr:")[1][0:4]) <= 2030 and int(passport.split("eyr:")[1][0:4]) >= 2020:
                                # print("eyr: " + passport.split("eyr:")[1][0:4] + " A ")

                                if passport.__contains__("hgt"):
                                    height = False;
                                    if passport.split("hgt")[1][0:6].__contains__("cm"):
                                        if int(passport.split("hgt:")[1].split("cm")[0]) >= 150 and int(passport.split("hgt:")[1].split("cm")[0]) <= 193:
                                            height = True
                                    elif passport.split("hgt")[1][0:6].__contains__("in"):
                                        if int(passport.split("hgt:")[1].split("in")[0]) >= 59 and int(passport.split("hgt:")[1].split("in")[0]) <= 76:
                                            height = True
                                    if height == True:
                                        if passport.__contains__("hcl"):
                                            if passport.split("hcl:")[1][0:7].startswith("#"):
                                                if passport.__contains__("ecl"):
                                                    col = ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]
                                                    if col.__contains__(passport.split("ecl:")[1][0:3]):
                                                        if passport.__contains__("pid"):
                                                            if passport.split("pid:")[1][0:9].isdigit():
                                                                    valid += 1
                                                                    print(passport.split("pid:")[1].split(" ")[0])
                                                                    if passport.split("pid:")[1][0:10].isdigit():
                                                                        try:
                                                                            passport.split("pid:")[1][9]
                                                                            valid -= 1
                                                                        except:
                                                                            valid += 0
        if len(points) == 7:
                valid += 0

        points = []
        passport = ""
    else:
        passport += i;

print(valid)





