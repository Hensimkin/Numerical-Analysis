def append1(matrix1,vec1):
    newmat=[]
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix1[0])):
            temp.append(matrix1[i][j])
        temp.append(vec1[i][0])
        newmat.append(temp)
    for i in range(len(matrix1)):
        print(newmat[i])
    print()
    return newmat


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def chechdominat2(matrix):
    count=0
    for i in range(len(matrix)):
        sum1=sum(matrix[i])
        if matrix[i][i]>sum1-matrix[i][i]:
            count+=1
    if count==len(matrix):
        print("The matrix has dominance")
    else:
        print("The matrix has no dominance")


def checkdominat(newmat,mat):
    for i in range(len(newmat)):
        sum1=sum(mat[i])
        if newmat[i][i]<sum1-newmat[i][i]:
            num=i+1
            raw=0
            count = 0
            while num!=len(newmat):
                sum2 = sum(mat[num])
                if newmat[num][i] > sum2 - newmat[num][i]:
                    raw=num
                    count+=1
                num+=1
            if count==1:
                newmat=swapPositions(newmat, i, raw)
                mat=swapPositions(mat, i, raw)
    for i in range(len(newmat)):
        print(newmat[i])
    print()
    return newmat


def f1(list,i,arr):
    temp=0
    temp2=list[len(list)-1]
    for j in range(len(list)-1):
        if j!=i:
            temp=temp+(list[j]*(-1))*arr[j]
    temp2=temp2+temp
    return temp2/list[i]


def final(matrix):
    count=1
    e=0.00001
    arr=[0,0,0]
    arr2=[0,0,0]
    arr3=[0,0,0]
    condition=True
    while condition:
        counter=0
        for i in range(len(matrix)):
            arr2[i]=f1(matrix[i],i,arr)
        print(count," ",end=" ")
        for i in range(len(matrix)):
            print('%0.4f\t' % arr2[i], end=" ")
        print(" ")
        count+=1
        for i in range(len(matrix)):
            arr3[i]=abs(arr[i] - arr2[i])
        for i in range(len(matrix)):
            arr[i]=arr2[i]
        for i in range(len(matrix)):
            if arr3[i]>e:
                counter+=1
        if counter == len(matrix):
            condition = True
        else:
            condition = False
    print('\nThe solution for the matrix is: ')
    for i in range(len(matrix)):
        print(f'x{i+1}=%0.3f' % arr2[i], end=" ")


def final2(matrix):
    count=1
    e=0.00001
    arr=[0,0,0]
    arr2=[0,0,0]
    arr3=[0,0,0]
    condition=True
    while condition:
        counter=0
        for i in range(len(matrix)):
            arr2[i]=f1(matrix[i],i,arr2)
        print(count," ",end=" ")
        for i in range(len(matrix)):
            print('%0.4f\t' % arr2[i], end=" ")
        print(" ")
        count+=1
        for i in range(len(matrix)):
            arr3[i]=abs(arr[i] - arr2[i])
        for i in range(len(matrix)):
            arr[i]=arr2[i]
        for i in range(len(matrix)):
            if arr3[i]>e:
                counter+=1
        if counter == len(matrix):
            condition = True
        else:
            condition = False
    print('\nThe solution for the matrix is: ')
    for i in range(len(matrix)):
        print(f'x{i+1}=%0.3f' % arr2[i], end=" ")


def choose():
    matrix2 = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]
    num=int(input("1. Jacobi \t 2. Gauss-Seidel\n"))
    if num==1:
        new = append1(matrix2, vectorB)
        checkdominat(new, matrix2)
        chechdominat2(matrix2)
        final(new)
    elif num==2:
        new = append1(matrix2, vectorB)
        checkdominat(new, matrix2)
        chechdominat2(matrix2)
        final2(new)
    else:
        print("Wrong choice")


choose()
"""""
matrix2=[20,1,-2],[3,20,-1],[2,-3,20]
vectorB=[[17], [-18], [25]]
matrix=[[4,2,0],[2,10,4],[0,4,5]]


matrix2=[[2,10,4],[0,4,5],[4,2,0]]
matrix=[[4,2,0],[2,10,4],[0,4,5]]
vectorB=[[2],[6],[5]]
"""""






