class Solution:
    def trap(self, height: List[int]) -> int:
        maxLength = len(height) - 1;

        result = 0;

        toRight = [0 for i in range(maxLength + 1)];
        toLeft = [0 for i in range(maxLength + 1)];

        toRight[0] = height[0];
        toLeft[maxLength] = height[maxLength]

        for i in range(1, len(height)): 
          toRight[i] = max(height[i], toRight[i-1]);
          toLeft[maxLength-i] =  max(height[maxLength-i], toLeft[maxLength+1-i]);

        for i in range(0, maxLength + 1):
          result += min(toLeft[i], toRight[i]) - height[i];
        
        return result;