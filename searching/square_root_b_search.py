def bs_sqrt(n):
    l=0
    h=n
    mid=(l+h)//2
    ans=-1
    while(l<=h):
        if(n==mid*mid):
            ans=mid
        if(n<mid*mid):
            h=mid-1
        else:
            ans=mid
            l=mid+1
        mid=(l+h)//2
    p=int(input("Enter the number of precision : "))
    step=0.1
    ans=float(ans)
    for _ in range(p):
        while(ans*ans<=n):
            ans+=step
        ans-=step
        step=step/10
    print(round(ans,p))

# bs_sqrt(10)
