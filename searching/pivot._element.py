class Solution:
    def search(self, a: List[int], target: int) -> int:
        l=0
        h=len(a)-1
        pivot=-1
        while(l<=h):
            mid=(l+h)//2
            if(l==h):
                pivot=l
                break
            if(mid<h) and a[mid]>a[mid+1]:
                pivot=mid
                break
            if(mid>l and a[mid]<a[mid-1]):
                pivot=mid-1
                break
            if(a[l]>a[mid]):
                h=mid-1
            else:
                l=mid+1
        if(pivot==-1):
            return self.bs(a,0,len(a)-1,target)
        if(target>=a[0] and target<=a[pivot]):
            return self.bs(a,0,pivot,target)
            
        else:
            return self.bs(a,pivot+1,len(a)-1,target)
        return -1
             
    def bs(self,a,l,h,k):
        while(l<=h):
            mid=(l+h)//2
            if(a[mid]==k):
                return mid
            elif(a[mid]>k):
                h=mid-1
            else:
                l=mid+1
        return -1

