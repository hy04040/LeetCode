# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def binary_search(n, p, r):
            if p<r:
                q = (p+r)//2
                if isBadVersion(q):
                    return binary_search(n,p,q)
                else:
                    return binary_search(n,q+1,r)
            return p
        bad_version = binary_search(n,1,n)
        return bad_version
            
        