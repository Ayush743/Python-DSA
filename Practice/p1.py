def binary_search(n,k):
    l=0
    h=len(n)-1
    while(l<=h):
        mid=(l+h)//2
        
        if(n[mid]==k):
            print(mid)
            break
        elif(k>n[mid]):
            l=mid+1
        else:
            h=mid-1

    
# binary_search([12,13,24,35,46,58,79,80,97],80)
def first_occ(n,k):
    l=0
    h=len(n)-1
    ans=-1
    while(l<=h):
        mid=(l+h)//2
        if(n[mid]==k):
            ans=mid
            l=mid+1
        elif(k>n[mid]):
            l=mid+1
        else:
            h=mid-1
    print(ans)
# first_occ([12,13,13,13,24,24,24,35,46,58,79,80,80,80,97],13   )
def peak_element(a):
    l=0
    h=len(a)-1
    mid=(l+h)//2
    while(l<h):
        mid=(l+h)//2
        if(a[mid]<a[mid+1]):
            l=mid+1
        else:
            h=mid
    print(h) #or print(l) as both h and l will be equal
# peak_element([0,10,15,13,4])
def sq(n):
    l=0
    h=n
    ans=-1
    while(l<=h):
        mid=(l+h)//2
        if(n==mid*mid):
            ans=mid
            break
        elif(n>mid*mid):
            l=mid+1
            ans=mid
        else:
            h=mid-1
        
    p=int(input("Enter the number of precision :"))
    s=0.1
    ans=float(ans)
    for _ in range(p):
        while(ans*ans<=n):
            ans+=s
            s=s/10
    print(round(ans,p))

        
sq(16)