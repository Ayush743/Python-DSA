#<<<<<<<<<----------Linear Search 0(n)------------------------>>>>>>>>>
def linear_search(l,k):
    for i in range(len(l)):
        if(l[i]==k):
            return 'present'
        else:
            return 'not present'
# print(linear_search([2,3,4,5,6,10,86,53,32],45))
#<<<<<<<<<<<<<<--------Binary Search------------------->>>>>>>>>
def binarySearch(n,s):
    l=0
    h=len(n)-1
    mid=(l+h)//2
    while(l<=h):
        if(s==n[mid]):
            return f'found at index {mid}'
        elif(s<n[mid]):
            h=mid-1
        else:
            l=mid+1
        mid=(l+h)//2
    return 'not found'
        

# print(binarySearch([2, 4, 24, 31, 42, 45, 54, 65],45))




#<<<--------first occurence using binary search----------------->
def f_occ(n,k):
    l=0
    h=len(n)-1
    mid=(l+h)//2
    while(l<=h):
            if(n[mid]==k):
                ans=mid 
                h= mid-1
            elif(n[mid]>k):
                h=mid-1
            else:
                l=mid+1
            mid=(l+h)//2
    print(ans)


# f_occ([1,2,2,6,3,4,5,6,67,7,7,7,7],7)

def last_occ(n,k):
    l=0
    h=len(n)-1
    mid=(l+h)//2
    while(l<=h):
        if(k==n[mid]):
            ans=mid
            l=mid+1
        elif(k>n[mid]):
            l=mid+1
        else:
            h=mid-1
        mid=(l+h)//2
    print('Last occurence of the element at :',ans)
# last_occ([1,1,2,2,2,2,3,3,4,4,4,4,4,4],2)
    


#<<<<<<<<<<<<<<<-----------Binary Search in 2-d Array----------->>>>>>>>>>>>>>>>>>>
import numpy as np
def bs_2d(r,c,k):
    z=np.array(list(map(int,input().split(',')))).reshape(r,c)
    l=0
    h=r*c-1
    mid=(l+h)//2
    while(l<=h):
        row=mid//c
        col=mid%c
        if(z[row][col]==k):
            print(True)
            return
        elif(mid>k):
            h=mid-1
        else:
            l=mid+1
        mid=(l+h)//2
    print(False)
bs_2d(3,4,6)



