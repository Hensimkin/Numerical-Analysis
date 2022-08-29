import random


def split(array):
    return [char for char in array]


def lottery(id_num):
    z=int(random.choice(split(id_num)))
    n=z%12
    print("The choice is :",n+19)


def final(matrix,elemtary):
    for i in range(len(matrix)):
        if matrix[i][i]!=1:

            j=i+1
            size=len(matrix)
            temp = 1 / matrix[i][i]
            elemtary[i][i] = temp
            savedmatrix(elemtary)
            temp=matrix
            matrix = mult(elemtary, matrix)
            printelementary2(elemtary,temp,matrix)
            elemtary = elemteryreset(matrix)
            pivot=matrix[i][i]
            while j<size:
                if matrix[j][i] != 0:
                    elemtary[j][i] = (matrix[j][i] * pivot) * (-1)
                    savedmatrix(elemtary)
                    temp2=matrix
                    matrix = mult(elemtary, matrix)
                    printelementary2(elemtary,temp2,matrix)
                    elemtary = elemteryreset(matrix)
                j+=1
    return matrix


def final2(matrix,elemtary):
    size=len(matrix)
    for i in range(len(matrix)-1,0,-1):
        j = i - 1
        while j >= 0:
            pivot = matrix[i][i]
            elemtary[j][i] = (matrix[j][i] * pivot) * (-1)
            savedmatrix(elemtary)
            temp=matrix
            matrix = mult(elemtary, matrix)
            printelementary2(elemtary,temp,matrix)
            elemtary = elemteryreset(matrix)
            j-=1
    return matrix

"""""
def final3(matrix,elemtary):
    for i in range(len(matrix)):
        j = 0
        pivot = matrix[i][i]
        while j < i:

            if matrix[j][i] != 0:
                elemtary[j][i] = (matrix[j][i] * pivot) * (-1)
                savedmatrix(elemtary)
                printelementary(elemtary)
                matrix = mult(elemtary, matrix)
                elemtary = elemteryreset()
            j += 1
    return matrix
"""""


def mult(matrix1,matrix2):
    res=[[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    size=len(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


def addmat(matrix1,matrix2):
    res=[[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            res[i][j] = matrix1[i][j] + matrix2[i][j]
    return res

def changerow(matrix,row1,row2):
    temp=matrix[row1]
    matrix[row1]=matrix[row2]
    matrix[row2]=temp
    return matrix


def findpivot(matrix, elemtary):
    biggest = 0
    size = len(matrix)
    for i in range(len(matrix)):
        j = i
        change = False
        saved = matrix[i][i]
        while j < size:
            if saved < matrix[j][i]:
                biggest = j
                saved = matrix[biggest][i]
                change = True
            j += 1
        if change:
            elemtary = changerow(elemtary, i, biggest)
            temp=matrix
            savedmatrix(elemtary)
            matrix = mult(elemtary, matrix)
            printelementary2(elemtary,temp,matrix)
        elemtary=elemteryreset(matrix)
    return matrix


def savedmatrix(matrix):
    totalmatrix.append(matrix)

def printelementary2(matrix1,matrix2,matrix3):
    for i in range(len(matrix1)):
        if i==1:
            print(matrix1[i],"    *    ",matrix2[i],"    =    ",matrix3[i])
        else:
            print(matrix1[i], "          ", matrix2[i], "         ", matrix3[i])
    print()
    print("*******************************************************")
    print()


def printelementary(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()
    print("*******************************************************")
    print()



def elemteryreset(matrix):
    return createlemtary(matrix)


def opposite():
    calc = [[0 for x in range(len(totalmatrix[0]))] for y in range(len(totalmatrix[0]))]
    calc=mult(totalmatrix[0],totalmatrix[1])
    for i in range(2,len(totalmatrix)):
        calc=mult(calc,totalmatrix[i])
    return calc


def opposite2():
    calc = [[0 for x in range(len(totalmatrix[0]))] for y in range(len(totalmatrix[0]))]
    calc=mult(totalmatrix[len(totalmatrix)-1],totalmatrix[len(totalmatrix)-2])
    for i in range(len(totalmatrix)-3,-1,-1):
        calc=mult(calc,totalmatrix[i])
    return calc


def determinantOfMatrix(mat, n):
    temp = [0] * n
    total = 1
    det = 1
    for i in range(0, n):
        index = i
        while mat[index][i] == 0 and index < n:
            index += 1
        if (index == n):
            continue
        if (index != i):
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
            det = det * int(pow(-1, index - i))
        for j in range(0, n):
            temp[j] = mat[i][j]
        for j in range(i + 1, n):
            num1 = temp[i]  # value of diagonal element
            num2 = mat[j][i]  # value of next row element
            for k in range(0, n):
                mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])
            total = total * num1  # Det(kA)=kDet(A);
    for i in range(0, n):
        det = det * mat[i][i]
    if int(det / total)==0:
        print("The determinate is 0 and there is no inverse matrix")
    else:
        return int(det / total)


def determinate(matrix,n):
    if n==2:
        sum=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return sum
    if n>2:
        sum=0
        for i in range(len(matrix[0])):
            if i%2==0:
                sum=(sum+(matrix[i][0])*(determinate((smalldet(matrix,i,0)),n-1)))
            else:
                sum = (sum - (matrix[i][0]) * (determinate((smalldet(matrix, i, 0)), n - 1)))
        return sum


def smalldet(matrix,n,m):
    newmatrix=[]
    for i in range(len(matrix)):
        newtemp=[]
        for j in range(len(matrix)):
            if i!=n and j!=m:
                newtemp.append(matrix[i][j])
        if len(newtemp)>0:
            newmatrix.append(newtemp)
    return newmatrix

def seperate(matrix):
    newmat=[]
    for i in range(len(matrix)):
        newmat2=[]
        for j in range(len(matrix[0])-1):
            newmat2.append(matrix[i][j])
        newmat.append(newmat2)
    return newmat


def createlemtary(matrix):
    big=[]
    if len(matrix)!=len(matrix[0]):
        size=len(matrix[0])-1
        for i in range(size):
            small=[]
            for j in range(size):
                if i==j:
                    small.append(1)
                else:
                    small.append(0)
            big.append(small)
        return big
    else:
        size = len(matrix[0])
        for i in range(size):
            small = []
            for j in range(size):
                if i == j:
                    small.append(1)
                else:
                    small.append(0)
            big.append(small)
        return big


def printfinalanswer(matrix):
    for i in range(len(matrix)):
        print("x",i+1," = ",matrix[i][3])

    print()
    print("*******************************************************")
    print()




def process(matrix):
    elementary=createlemtary(matrix)
    if len(matrix)!=len(matrix[0]):
        matrix2=seperate(matrix)
        if determinate(matrix2, len(matrix2)) == 0:
            print("Cant find the solution, no inverse matrix")
        else:
            matrix = findpivot(matrix, elementary)
            elementary = elemteryreset(matrix)
            matrix = final(matrix, elementary)
            elementary = elemteryreset(matrix)
            matrix = final2(matrix, elementary)
            printfinalanswer(matrix)
            print("total elementarys number :",len(totalmatrix))

    else:
        if determinate(matrix, len(matrix)) == 0:
            print("Cant find the solution, no inverse matrix")
        else:
            matrix = findpivot(matrix, elementary)
            elementary = elemteryreset(matrix)
            matrix = final(matrix, elementary)
            elementary = elemteryreset(matrix)
            matrix = final2(matrix, elementary)
            printfinalanswer(matrix)
            print(len(totalmatrix))


lottery(input(" endter id"))
totalmatrix=[]
lmt = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
mat3=[[1,1,1],[1,2,4],[1,3,9]]
process(mat3)


