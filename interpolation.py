from random import choice


def f(x1,y1,x2,y2,point):
    return(((y1-y2)/(x1-x2))*point)+((y2*x1-y1*x2)/(x1-x2))


def linear(table,point):
    i=0
    while table[i][0]<=point:
        i+=1
    i=i-1
    if i==len(table)-1 or i==0:
        print("The point is outside bounds")
    elif i==point:
        print(table[i][0],table[i][1])
    else:
        p=round(f(table[i][0],table[i][1],table[i+1][0],table[i+1][1],point),6)
        print("the point of",point,"is",p)



def polynom(table,point):
    if len(table)<3:
        print("cant calculate")
    else:
        i=0
        mat=[[1],[1],[1]]
        vec=[[],[],[]]

        while table[i][0]<point and table[i+1][0]<point and table[i+2][0]<point:
            i+=1
        mat[0].append(table[i][0])
        mat[0].append((table[i][0]) ** 2)
        mat[1].append(table[i + 1][0])
        mat[1].append((table[i + 1][0]) ** 2)
        mat[2].append(table[i + 2][0])
        mat[2].append((table[i + 2][0]) ** 2)
        vec[0].append(table[i][1])
        vec[1].append(table[i + 1][1])
        vec[2].append(table[i + 2][1])
        """""
        a=choice(table)
        if a==table[len(table)-2] or a==table[len(table)-1]:
            a=table[len(table)-3]
        mat[0].append(a[0])
        mat[0].append(a[0]**2)
        vec[0].append(a[1])
        b=a
        while b==a or (b[0]<a[0]):
            b=choice(table)
        if b==table[len(table)-1]:
            b=table[len(table)-2]
        mat[1].append(b[0])
        mat[1].append(b[0] ** 2)
        vec[1].append(b[1])
        c=a
        while (c==a or c==b) or c[0]<b[0]:
            c=choice(table)
        mat[2].append(c[0])
        mat[2].append(c[0] ** 2)
        vec[2].append(c[1])
        
        #mat=[[1,1,1],[1,2,4],[1,3,9]]
        vec=[[0.8415],[0.9093],[0.1411]]
        mat=getMatrixInverse(mat)
        
        mat = [[1, 2, 4], [1, 3, 9], [1, 4, 16]]
        vec = [[0.9093], [0.1411],[-0.7568]]
        """""
        mat=getMatrixInverse(mat)
        g=mult(mat,vec)
        sum=g[0][0]+(g[1][0]*point)+(g[2][0]*(point**2))
        print("the point of",point,"is",round(sum,5))




def transposeMatrix(m):
    a= list(map(list,zip(*m)))
    return a

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = round(getMatrixDeternminant(m),6)
    if len(m) == 2:
        return [[round(m[1][1]/determinant,6), round(-1*(m[0][1]/determinant),6)],
                [round(-1*(m[1][0]/determinant),6), round(m[0][0]/determinant,6)]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def mult(matrix1,matrix2):
    res=[[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    size=len(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


def multiply(v, G):
    result = []
    for i in range(len(G[0])):
        total = 0
        for j in range(len(v)):
            a=round((G[j][i])*(v[j]),6)
            total = total+a
        result.append(total)
    return result



def multiply2(v, G):
    result = []
    for i in range(len(G[0])):
        total = 0
        for j in range(len(v)):
            a=round((G[i][j])*(v[j]),6)
            total = round(total+a,5)
        result.append(total)
    return result





def transposeMatrix(m):
    a= list(map(list,zip(*m)))
    return a

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant




def lagrange(table,point):
    pn=0
    for i in range(len(table)):
        ln=0
        for j in range(len(table)):
            if i!=j:
                if ln==0:
                  ln+=(point-table[j][0])/(table[i][0]-table[j][0])
                else:
                    ln *= (point - table[j][0]) / (table[i][0] - table[j][0])
        pn+=table[i][1]*ln
    print("The value of f(",point,") is :",round(pn,4))

def nevile(table, point):
    myarr=[[0 for col in range(len(table))]for row in range(len(table))]
    for i in range(len(table)):
        if i==0:
            for j in range(len(table)):
                myarr[j][j]=table[j][1]
        else:
            for k in range(len(table)):
                if k+i<len(table):
                 myarr[k][k+i]=(((point-table[k][0])*myarr[k+1][k+i])-((point-table[k+i][0])*myarr[k][k+i-1]))/(table[k+i][0]-table[k][0])
    print("The value of f(", point, ") is :",round(myarr[0][len(table)-1],5) )






def splinecubic(table,point):
    distances=[]
    a=0
    b=0
    for i in range(len(table)-1):
        distances.append(round(table[i+1][0]-table[i][0],6))
        if table[i][0]<point and table[i+1][0]>point:
            a=i
            b=i+1
    matrix = [[0 for col in range(len(table)-2)] for row in range(len(table)-2)]
    d=[]
    print(distances)
    for j in range(len(matrix)):
        for k in range(len(matrix)):
            if k==j:
                matrix[j][k]=2
            if k==j+1 and j+1<len(matrix):
                matrix[j][k]=round(distances[j+1]/(distances[j]+distances[j+1]),6)
            if k+1==j and k+1<len(matrix):
                matrix[j][k]=round(1-(distances[j+1]/(distances[j]+distances[j+1])),6)
        ck=round(6/round((distances[j]+distances[j+1]),5),6)
        ck2=round(((table[j+2][1]-table[j+1][1])/distances[j+1])-((table[j+1][1]-table[j][1])/distances[j]),6)
        ck3=round(ck*ck2,6)
        #d.append((6/(distances[j]+distances[j+1]))*(((table[j+2][1]-table[j+1][1])/distances[j+1])-((table[j+1][1]-table[j][1])/distances[j])))
        d.append(ck3)
    print(matrix)
    print(d)

    matrix=getMatrixInverse(matrix)
    s=multiply2(d,matrix)
    print(s)
    if a==0:
        mi=0
    else:
        mi=s[a-1]
    if b+1==len(table):
        mi1=0
    else:
        mi1=s[b-1]
    print(mi, mi1)


    x=(((((table[b][0]-point)**3)*mi)+((point-table[a][0])**3)*mi1))/(6*distances[a-1])
    print(round(x,5))
    y=(((table[b][0]-point)*table[a][1])+((point-table[a][0])*table[b][1]))/distances[a]
    print(round(y,5))


    z=(((table[b][0]-point)*mi)+(((point-table[a][0])*mi1)*distances[a-1]))/6
    print(round(z,5))
    """""
    x=((((table[b][0]-point)**3)*mi)+(((point-table[a][0])**3)*mi1))/(6*distances[1])
    y=(((table[b][0]-point)*table[a][1])/distances[2])
    z=((((table[b][0]-point)*mi)+((point-table[a][0])*mi1))*distances[2])/6
    """""
    sk=round(x+y-z,6)
    print("The value of f(", point, ") is :",round(sk,5))









"""""
mat3=[[1,1,1],[1,2,4],[1,3,9]]
arr=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9585],[6,-0.2794]]
point=2.5
#linear(arr,point)
polynom(arr,point)
"""""



def main():
    #print("Choose :\n 1.Liniar \n2.polynom \n3.lagrange\n4.nevile\n5.splinecubic\n6.exit")
    a=-2
    #a=int(input())
    while a!=200:
        print("Choose :\n 1.Liniar \n2.polynom \n3.lagrange\n4.nevile\n5.splinecubic\n6.exit")
        a = int(input())
        if a == 1:
            arr = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9585], [6, -0.2794]]
            point = 2.5
            linear(arr, point)
        elif a == 2:
            arr = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9585], [6, -0.2794]]
            point = 2.5
            polynom(arr, point)
        elif a == 3:
            arr3 = [[1, 1], [2, 0], [4, 1.5]]
            point2 = 3
            lagrange(arr3, point2)
        elif a == 4:
            arr5 = [[1, 0], [1.2, 0.112463], [1.3, 0.167996], [1.4, 0.222709]]
            point = 1.28
            nevile(arr5, point)
        elif a == 5:
            arr2 = [[0, 0], [round(pie / 6, 5), 0.5], [round(pie / 4, 5), 0.7072], [round(pie / 2, 5), 1]]
            point = round(pie / 3, 5)
            splinecubic(arr2, point)
        elif a == 6:
            a=200
            print("goodbye")
        elif a>6:
            print("Wrong choice")



pie=3.14159
main()

