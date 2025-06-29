def div_b_s(divident,divisor):
    l=0
    dd,ds=abs(divident),abs(divisor)
    h=dd
    ans=-1
    while(l<=h):
        mid=(l+h)//2
        if(dd==mid*ds):
            ans=mid
            break
        elif(dd<mid*ds):
            h=mid-1
        else:
            ans=mid
            l=mid+1
    
    if(divident<0 and divisor<0 ):
        return ans
    elif(divisor<0 or divident<0):
        return -ans
    else:
         return ans
# print(div_b_s(21,-7))

# print(chr(65))
def power(m,i):
    a=1
    for _ in range(i):
        a*=m
        
        
    print(a)
power(2,5)
