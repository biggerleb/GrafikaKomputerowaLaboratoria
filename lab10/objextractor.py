fOBJ = open("Ludzik.obj", "r")
verticesList = []
verticesList.append("Dummy element")
indexesList = []
normalsList = []
normalsList.append("Dummy element")
for l in fOBJ:
    lineList = l.split()
    if lineList[0] == "v":
        # print(lineList)
        verticesList.append(lineList)
    if lineList[0] == "f":
        lineList[1] = lineList[1].split("/")
        lineList[2] = lineList[2].split("/")
        lineList[3] = lineList[3].split("/")
        indexesList.append(lineList)
    if lineList[0] == "vn":
        normalsList.append(lineList)
fOBJ.close()

fVertices = open("vertices.txt", "w")
fNormals = open("normals.txt", "w")
for el in indexesList:
    fVertices.write("vertexPosition.push(...[" + str(verticesList[int(el[1][0])][1]) + ", " + str(verticesList[int(el[1][0])][2]) + ", " + str(verticesList[int(el[1][0])][3]) + "]);" + "\n") # v1
    fVertices.write("vertexPosition.push(...[" + str(verticesList[int(el[2][0])][1]) + ", " + str(verticesList[int(el[2][0])][2]) + ", " + str(verticesList[int(el[2][0])][3]) + "]);" + "\n") # v2
    fVertices.write("vertexPosition.push(...[" + str(verticesList[int(el[3][0])][1]) + ", " + str(verticesList[int(el[3][0])][2]) + ", " + str(verticesList[int(el[3][0])][3]) + "]);" + "\n") # v3
    
    fNormals.write("vertexNormal.push(...[" + str(normalsList[int(el[1][2])][1]) + ", " + str(normalsList[int(el[1][2])][2]) + ", " + str(normalsList[int(el[1][2])][3]) + "]);" + "\n") # v1
    fNormals.write("vertexNormal.push(...[" + str(normalsList[int(el[2][2])][1]) + ", " + str(normalsList[int(el[2][2])][2]) + ", " + str(normalsList[int(el[2][2])][3]) + "]);" + "\n") # v2
    fNormals.write("vertexNormal.push(...[" + str(normalsList[int(el[3][2])][1]) + ", " + str(normalsList[int(el[3][2])][2]) + ", " + str(normalsList[int(el[3][2])][3]) + "]);" + "\n") # v3 
fVertices.close()
fNormals.close()


# verticesList  [ [0]'v' [1]x [2]y [3]z ]
# indexesList [ [0]'f' [1][v1, vt1, vn1] [2][v2, vt2, vn2] [3][v3, vt3, vn3] ]