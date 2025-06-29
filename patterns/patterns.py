#square pattern
def square(n):
    for i in range(n):
        for j in range(n):
            print('*',end=" ")
        print()

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or j==n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
        
def hollow_inverted_pyramid(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or j==n-i-1):
                print("*",end=" ")
           
            else:
                print(" ",end=" ")
        print()
def pyramid(n):

    for i in range(n):
        k=0
        for j in range(2*n-1):
            if(j<n-i-1):
                print(" ",end=" ")
            elif(k<2*i+1):
                print("*",end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()

def sp(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1): #2i+1,
            print("* ",end=" ")
        print()
def re(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(n-i):
            print("* ",end=" ")
        print()
def dia(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ",end= ' ')
        for j in range(i+1):
            print("* ",end=" ")
        print()
    for i in range(n):
        for j in range(i):
            print(" ",end= " ")
        for j in range(n-i):
            print("* ",end= " ")
        print()

def hin(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ",end= " ")
        for j in range(2*n+1):
            if(j==0 or j==2*i):
                print("*",end=" ")
            else:
                print(" ",end= " ")
        print()
def hina(n):
   for i in range(n):
        for j in range(n-i):
           print("*",end=" ")
        for j in range(2*i+1):
            print(" ",end=" ")
        for j in range(n-i):
           print("*",end=" ")
        print()
   for i in range(n):
        for j in range(i+1):
           print("*",end=" ")
        for j in range(2*n-2*i-1):
            print(" ",end=" ")
        for j in range(i+1):
           print("*",end=" ")
        print()
def hi(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
            if(i!=j):
                print("*",end="")
        print()
    for i in range(n,0,-1):
        for j in range(i):
            print(i,end="")
            if(i!=j+1):
                print("*",end="")
        print()
def hinata(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        for j in range(j-1,0,-1):
                print(j,end= "")
        print()
hinata(5)