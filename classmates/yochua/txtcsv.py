file = open("met_per.txt", "r")
dataFile = file.read().split("\n")
dataFile.pop()
dataFile.pop()
dataY = [list(map(int,i.split("\t"))) for i in dataFile]

file.close()

file = open("met_per.csv", "w")
for i in dataY: 
    st = ""
    for j in i:
        st += str(j) + ","
    st = st[:(len(st)-1)]
    st += "\n"
    file.write(st)

