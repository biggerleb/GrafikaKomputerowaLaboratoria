word = ""
fIN = open("input.txt", "r")
fOUT = open("output.txt", "w")
x = 0
while True:
    line = fIN.readline()
    lineArr = line.split()
    if len(lineArr) == 5:
        x += 2
        x1 = int(lineArr[1])
        y1 = int(lineArr[2])
        x2 = int(lineArr[3])
        y2 = int(lineArr[4])
        if lineArr[0] == "H":
            result =  str(x1) + ", " + str(y1 - 0.1) + ", 0,   " + str(x1) + ", " + str(y1 + 0.1) + ", 0,   " + str(x2) + ", " + str(y2 + 0.1) + ", 0,   \n"
            result += str(x2) + ", " + str(y2 - 0.1) + ", 0,   " + str(x2) + ", " + str(y2 + 0.1) + ", 0,   " + str(x1) + ", " + str(y1 - 0.1) + ", 0,   \n"
        if lineArr[0] == "V":
            result =  str(x1-0.1) + ", " + str(y1) + ", 0,   " + str(x1+0.1) + ", " + str(y1) + ", 0,   " + str(x2-0.1) + ", " + str(y2) + ", 0,   \n"
            result += str(x2-0.1) + ", " + str(y2) + ", 0,   " + str(x2+0.1) + ", " + str(y2) + ", 0,   " + str(x1+0.1) + ", " + str(y1) + ", 0,   \n"
        fOUT.write(result)

    else:
        break

print(x)
fIN.close()
fOUT.close()