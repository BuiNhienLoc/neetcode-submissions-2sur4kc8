class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0

        i = 0
        j = len(heights)-1
        while i!=j:
            area = (j-i) * min(heights[i],heights[j])
            
            if area > max:
                max = area
            
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            elif heights[i] == heights[j]:
                j-=1 
            
        return max
            

    