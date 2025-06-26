import numpy as np
arr=np.array([[1,2,3],[4,5,6],[2,6,8]])
def two_d(arr):
    for i in range(3):
        for j in range(3):
           print(arr[j][i],end=" ") #arr[i][j] for row wise and arr[j][i] for column wise
    print()

def inp_arr(r,c):
    arr=np.empty((r,c),int)
    for i in range(r):
        for j in range(c):
           arr[i][j]=int(input())
        print()
    print(arr)
        
    
    
# inp_arr(3,4)

def row_sum(r,c):
    z=list(map(int,input().split()))
    arr=np.array(z).reshape(r,c)
    print(arr)
    # for i in arr:
    #     s=0
    #     for j in i:
    #           s+=j
    #     print(s,end=" ")
    for i in range(r):
        s=0
        for j in range(c):
            s+=arr[i][j]
        print(s,end=" ")

# row_sum(3,3)
def col_sum(r,c):
    z=list(map(int,input().split()))
    arr=np.array(z).reshape(r,c)
    print(arr)
    for  i in range(c):
        s=0
        for j in range(c):
             s+=arr[j][i]
        print(s,end=" ")
# col_sum(3,3)
def td_s(r,c,s):
    z=list(map(int,input().split()))
    arr=np.array(z).reshape(r,c)
    k=0
    for i in range(r):
        for j in range(c):
            if(s==arr[i][j]):
                return True
    return False
   
# print(td_s(3,3,24))
def max_td(r,c):
    z=list(map(int,input().split(" ")))
    arr=np.array(z).reshape(r,c)
    maxy=arr[0][0]
    print(arr)
    for i in range(r):
        for j in range(c):
            if(maxy<arr[i][j]):
                maxy=arr[i][j]
    print(maxy)
# max_td(3,3)
def transpose_2d(r,c):
    z=list(map(int,input().split(" ")))
    arr=np.array(z).reshape(r,c)
    print(arr)
    tr=np.empty((c,r),int)
    for i in range(r):
        for j in range(c):
            tr[j][i]=arr[i][j]
    print()
    print()
    print()
    print(tr)
    
# transpose_2d(4,3)





