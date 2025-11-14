class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newArray = []
        for i in nums1:
            newArray.append(i)

        for j in nums2:
            newArray.append(j)

        newArray.sort()
        n=len(newArray)
        if n % 2==1:
            median = newArray[n//2]
        else:
            median1 = newArray[(n//2)-1]
            median2 = newArray[(n//2)]
            median = (median1+median2)/2.0

        return median

        