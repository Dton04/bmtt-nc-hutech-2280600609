input = input("Nhập X,Y:")
kichthuoc = [int(x) for x in input.split(",")]
rowNum = kichthuoc[0]
colNum = kichthuoc[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)