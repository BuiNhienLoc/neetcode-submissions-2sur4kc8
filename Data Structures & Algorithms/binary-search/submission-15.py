class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)//2
        visited = []

        while 0<=i and i<len(nums):
            visited.append(i)
            if nums[i] < target and i<=len(nums)-1:
                i+=1
            elif nums[i] > target and i>0:
                i-=1
            elif nums[i] == target:
                return i
            if i in visited or i>len(nums)-1:
                return -1



        return -1