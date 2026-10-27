class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft=[0]*len(height)
        maxRight=[0]*len(height)

        maxLeft[0]=height[0]
        for i in range(1,len(height)):
            maxLeft[i]=max(maxLeft[i-1],height[i])
        
        maxRight[len(height)-1]=height[len(height)-1]

        for i in range(len(height)-2,-1,-1):
            maxRight[i]=max(maxRight[i+1],height[i])
        sum=0
        for i in range(len(height)):
            height[i]=min(maxLeft[i],maxRight[i])-height[i]
            sum+=height[i]
        return sum
        

        