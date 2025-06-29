def b_s(n,k):
    l=0
    h=len(n)-1
    mid=(l+h)//2
    while(l<=h):
        if(n[mid]==k):
            return f'{k} at index : {mid}'
        elif( mid+1<=len(n) and n[mid+1]==k):
            return f'{k} at index : {mid+1}'
        elif(mid-1>=0 and  n[mid-1]==k):
            return f'{k} at index : {mid-1}'
        
        elif(n[mid]<k):
            l=mid+2
        else:
            h=mid-2
        mid=(l+h)//2
    return -1
print(b_s([10,3,40,20,50,80,70],50))
