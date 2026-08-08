class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        print(prefix_sum)
        
        hashmap={0:1}
        count=0
        for j in range(len(nums)):
            
            if prefix_sum[j]-k in hashmap:
                count+=hashmap[prefix_sum[j]-k]
            hashmap[prefix_sum[j]]=hashmap.get(prefix_sum[j],0)+1
            
            
           
        return count