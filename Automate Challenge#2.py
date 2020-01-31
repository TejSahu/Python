tableData = [['Apples', 'Oranges', 'Cherries', 'Banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['Dogs', 'Cats', 'Moose', 'Goose']]


def printtable():
    col_width = [0] * len(tableData)
    for a in range(len(tableData)):
        for b in range(len(tableData[a])):
            if col_width[a] < len(tableData[a][b]):
                col_width[a] = len(tableData[a][b])

    # print(col_width)  # -----[8,5,5]

    for a in range(0, 4):
        b = 0
        print(tableData[b][a].rjust(col_width[b]), tableData[b+1][a].rjust(col_width[b+1]),
              tableData[b+2][a].rjust(col_width[b+2]))


printtable()

#
# print(tableData[0][0], tableData[1][0],tableData[2][0])
# print(tableData[0][1], tableData[1][1],tableData[2][1])
# print(tableData[0][2], tableData[1][2],tableData[2][2])
# print(tableData[0][3], tableData[1][3],tableData[2][3])
