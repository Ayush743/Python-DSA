# #unique elements
# l=[1,1,2,3,4,5,66,54,3,54,6,6,7,8,7]
# s=[]
# for i in l:
#     if(l.count(i)==1):
#         print(i,end=" ")
def uniqueInteger(l):
    ans=0
    for i in range(len(l)):
        ans=ans^l[i]
    return ans
def uniqueElement():
    n=int(input("Enter the size of the array :"))
    print("Input the elements :")
    l=[]
    for i in range(n):
        m=int(input())
        l.append(m)
    print(l)
    ans=uniqueInteger(l)
    print(ans)
# uniqueElement()
def unionArray(a,b):
    c=[]
    for i in a:
        c.append(i)
    for j in b:
        c.append(j)
    print(c)
# unionArray([1,2,3,4],[5,6,7,8])
# def ls(l,a):
#     s=0
#     for i in range(len(l)):
#         if(a==l[i]):
#             s+=1
#     return s
        
def intersectionArray(a,b):
    l=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                b[j]='a'
                l.append(a[i])
    #    if(ls(b,a[i])):
    #        l.append(a[i])

    print(l) 
           
    
# intersectionArray([1,2,3,4,5,6,5,4,3,6,7,8],[1,2,3,4,7,8,9,5,4])

def twosum(l,k):
    z=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
                if(k==(l[i]+l[j])):
                    z.append((l[i],l[j]))
            
    print(z)
# twosum([1,2,3,4,5,6],7)

def threesum(l,sum):
    z=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                if(sum==(l[i]+l[j]+l[k])):
                    z.append((l[i],l[j],l[k]))
    print(z)
                     
                
    

# threesum([10,20,30,40],80)


def sort_0_1(l):
    l.sort()
    print(l)
    
#     end=len(l)-1
#     while(i<=end):
#         if(l[i]==0):
#             l[i],l[start]=l[start],l[i]
#             start+=1
#             i+=1
#         else:
#             l[i],l[end]=l[end],l[i]
#             end-=1
        
#     print(l)
        
# print(sort_0_1([1,0,0,0,1,0,1,1,1,0,0,1,0,1]))
def so(l):
    s,i=0,0
    e=len(l)-1
    while(s<=e):
        if(l[i]==0):
            l[i],l[s]=l[s],l[i]
            i+=1
            s+=1
        else:
            l[e],l[i]=l[i],l[e]
            e-=1
    print(l)
# so([1,1,0,0,1,1,0,1,0,1,1,0,0,1])
#<------------------------------Questions------------------------------------->
# move the -ve numbers to left side using 2 pointer approach
def tpa(arr):
    i=0
    s=0
    e=len(arr)-1
    while(i<=e):
        if(arr[i]<0):
            arr[i],arr[s]=arr[s],arr[i]
            i+=1
            s+=1
        else:
            arr[i],arr[e]=arr[e],arr[i]
            e-=1
    print(arr)
# tpa([1,2,-3,4,-5,6,0])
def three_pointer(nums):
    l,m=0,0
    h=len(nums)-1
    while(m<=h):
        if(nums[m]==0):
            nums[l],nums[m]=nums[m],nums[l]
            l+=1
            m+=1
        elif(nums[m]==1):
            m+=1
        else:
            nums[m],nums[h]=nums[h],nums[m]
            h-=1
    print(nums)
# three_pointer([2,0,1,0,2,2,0,1,0])
def find_duplicate(l):
    l.sort()
    for i in range(len(l)-1):
        if(l[i]==l[i+1]):
            return l[i]
# print(find_duplicate([1,2,3,3]))



#<<<<<<<<<-------negative index marking-------->>>>>>>>>>>>>>>


def neg_ind(l):
    ans=-1
    for i in range(len(l)):
        index=abs(l[i])
        if(l[index]<0):
            ans=index
            break
        l[index]*=-1
    print(ans)
# neg_ind([1,2,2,2,3])

def hi(n):
    while(n[0]!=n[n[0]]):
        n[n[0]],n[0]=n[0],n[n[0]]
    print(n[0])
# hi([1,2,2,2,3])
a=1
b=2
a,b=b,a
# print(a,b)
def find_dup(l):
    ans=-1

    for i in range(1,len(l)+1):
            index=abs(l[i])
            if(l[index]<0):
                ans=index
                break
            l[index]*=-1
    print(l)

# find_miss([1,2,2,3,4])
def find_miss(n):
    for i in range(len(n)):
        index=abs(n[i])
        if(n[index-1]>0):
            n[index-1]*=-1
    for i in range(len(n)):
        if(n[i]>0):
            print(i+1,end=" ")
# find_miss([1,3,3,3,2])
def first_repeat(n):
    d={}
    for i in n:
        if(i  in d):
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if(d[i]>1):
            print(i)
            break
        
# first_repeat([1,3,2,3,4,5])
def three_arr_common(a,b,c,x,y,z):
    i,j,k=0,0,0
    l=[]
    while(i<x and j<y and k<z):
                    if(a[i]==b[j] and b[j]==c[k]):
                        l.append(a[i])
                        i+=1
                        j+=1
                        k+=1
                    elif(a[i]<b[j]):
                        i+=1
                    elif(b[j]<c[k]):
                        j+=1
                    else:
                        k+=1
                           
    return l


# print(three_arr_common([1,1,2,2,3,4],[1,4,21,23,24],[1,4,11,48,69,79],6,5,5))
# a=[1,2,3,45]
# a.remove(2)
# print(a)


import numpy as np

def waveprint(r,c):
    z=np.array(list(map(int,input().split()))).reshape(r,c)
    print(z)
    for j in range(c):
        if(j%2==0):
            for i in range(r):
                print(z[i][j],end=" ")
        else:
            for i in range(r-1,-1,-1):
                print(z[i][j],end=" ")
# waveprint(3,4)


def calc_Sum ( a, b) : 
        #Complete the function
        i=len(a)-1
        j=len(b)-1
        c=0
        s=""
        while(i>=0 and j>=0):
            sum=a[i]+b[j]+c
            s+=str(sum%10)
            c=sum//10
            i-=1
            j-=1
        while(i>=0):
            sum=a[i]+0+c
            s+=str(sum%10)
            c=sum//10
            i-=1
          
        while(j>=0):
            sum=0+b[j]+c
            s+=str(sum%10)
            c=sum//10
            j-=1
        while(c):
            s+=str(c)
            c=0
            
        print(s[::-1])
 


# calc_Sum([1,2,3,4],[2,3])

            
