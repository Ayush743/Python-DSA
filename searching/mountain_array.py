def peakIndexInMountainArray(a):
        l=0
        h=len(a)-1
        while(l<h):
            mid=(l+h)//2
            if(a[mid]<a[mid+1]):
                  l=mid+1
            else:
                  h=mid
        print(h)
peakIndexInMountainArray([0,10,5,2])