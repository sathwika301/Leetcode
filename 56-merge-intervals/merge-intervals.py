class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]
        for intv in intervals:
            if not merged or merged[-1][1]<intv[0]:
                merged.append(intv)
            else:
                merged[-1][1]=max(merged[-1][1],intv[1])
        return merged