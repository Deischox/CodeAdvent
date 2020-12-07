import numpy as np
input = open("seats.txt","r").read().splitlines()
id = []
for s in input:
    row = [0, 127]
    seat = [0, 7]
    for i in s:
        if i == "F":
            lower = row[1]
            lower = row[1]-(((lower+1)-(row[0]))/2)
            row[1] = lower
        elif i == "B":
            lower = row[1]
            lower = row[0] + (((lower + 1) - (row[0])) / 2)
            row[0] = lower
        elif i  == "L":
            lower = seat[1]
            lower = seat[1] - (((lower + 1) - (seat[0])) / 2)
            seat[1] = lower
        elif i == "R":
            lower = seat[1]
            lower = seat[0] + (((lower + 1) - (seat[0])) / 2)
            seat[0] = lower
    id.append(int(row[0]*8+seat[0]))
id = np.array(id)
id = np.sort(id)

i = 0
while i < len(id):
    if i != len(id)-1:
        if id[i]+1 != id[i+1]:
            print(id[i]+1)
    i += 1