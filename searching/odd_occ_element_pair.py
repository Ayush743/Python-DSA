def odd_occ(a):
    l=0
    h=len(a)-1
    while(l<=h):
        mid=(l+h)//2
        if(mid%2==0):
            if(l==h):
                print(l)
                break
            if(a[mid]==a[mid+1]):
                l=mid+2
            else:
                h=mid
        else:
            if(a[mid]==a[mid-1]):
                l=mid+1
            else:
                h=mid-1
odd_occ([1,1,2,2,3,3,5,5,9,10,10])
          
