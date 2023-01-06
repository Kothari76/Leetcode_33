class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,b = 0 , len(nums)-1
        while a<=b:
            m = (a+b)//2
            if target == nums[m]:
                return m
            if nums[a]<=nums[m]:
                if target>nums[m] or target<nums[a]:
                    a = m+1
                else:
                    b = m-1
            else:
                if target<nums[m] or target>nums[b]:
                    b = m-1
                else:
                    a = m+1
        return -1
            
