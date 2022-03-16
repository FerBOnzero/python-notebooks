class Solution:
    def pathOfLIS(self, nums: List[int]):
        sub = []
        subIndex = []  
        path = [-1] * len(nums)  
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                path[i] = -1 if len(subIndex) == 0 else subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect_left(sub, x) 
                path[i] = -1 if idx == 0 else subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        ans = []
        t = subIndex[-1]
        while t >= 0:
            ans.append(nums[t])
            t = path[t]
        return ans[::-1]

print(Solution().pathOfLIS([2, 6, 8, 3, 4, 5, 1]))