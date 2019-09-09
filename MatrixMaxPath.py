#As per the question the execution should go to the right and then move down.

def CreateMatrix():
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))

    # Initialize matrix
    #matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(row):  # A for loop for row entries
        a = []
        for j in range(column):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    # For printing the matrix
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()
    LargestSum(row, column)

def LargestSum(row,column):
    #print(row,column)
    for i in range(row):
        sum = 0
        for j in range(column):
            sum += matrix[i][j]
        sum += sum
        if valuelist[0] < sum:
            valuelist[0] = sum
            valuelist[1] = i

    # for i in range(1,row):
    #     x = i-1
    #     sum = 0
    #     #print("dom")
    #     for j in range(column):
    #         sum += (matrix[i][j] + matrix[x][j])
    #         #print(sum)
    #         #print(valuelist[0])
    #     if valuelist[0] < sum:
    #         print("entered")
    #         valuelist[0] = sum
    #         valuelist[1] = x
    #         valuelist[2] = i

    for i in range(row):
        for x in range(row-1,i,-1):
            sum = 0
            for j in range(column):
                sum += matrix[i][j]
                sum += matrix[x][j]
            if x - i > 1:
                r = i+1
                for _ in range(r,x):
                    sum += matrix[_][column-1]
                    #print(matrix[_][column-1])
            if valuelist[0] < sum:
                # print("entered")
                valuelist[0] = sum
                valuelist[1] = i
                valuelist[2] = x

    if valuelist[1] < valuelist[2]:
        print("Entry @ row",valuelist[1]+1)
        print("Exit @ row",valuelist[2]+1)
    else:
        print("Entry @ row", valuelist[1] + 1)
        print("Exit @ row", valuelist[1] + 1)
    #print(valuelist)



    row = 0
    column = 0
if __name__=="__main__":
    matrix = []
    valuelist = [0,0,0]
    #valuelist.append(0)
    CreateMatrix()
    #LargestSum()