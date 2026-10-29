class Solution:
    def trap(self, height: list[int]) -> int:
        maxleftheight=[0] * len(height)
        maxrightheight=[0] * len(height)

        sum=0
        maxleftheight[0]=height[0]
        maxrightheight[len(height)-1]=height[len(height)-1]

        for i in range(len(height)):
            maxleftheight[i]=max(maxleftheight[i-1],height[i])
        
        for i in range(len(height)-2,-1,-1):
            maxrightheight[i]=max(maxrightheight[i+1],height[i])

        for i in range(len(height)):
            height[i]=min(maxleftheight[i],maxrightheight[i])-height[i]
            sum+=height[i]
        return sum
        
        

        