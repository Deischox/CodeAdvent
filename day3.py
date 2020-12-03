slope = open("slope.txt", "r").read().splitlines()

count = 0
trees = 0
counter = 1
i = 1
while i < 8:
    for row in slope:
        if row[count] == "#":
            trees += 1
        count += i
        if count >= 31:
            count = count%31

    counter *= trees
    count = 0
    trees = 0
    i += 2

l = 1
for row in slope:
    if l != 0:
        if row[count] == "#":
            trees += 1
        count += 1
        if count >= 31:
            count = count%31
    l += 1
    l = l%2

print(trees)

print(counter*trees)