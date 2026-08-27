class Solution(object):
    def removeElement(self, nums, val):
        k=0
        t=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[t]=nums[i]
                t+=1
            else:
                k+=1
        return t

    