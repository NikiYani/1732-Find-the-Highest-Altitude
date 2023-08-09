class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        v = []
        
        v.append(0)

        for i in range(0, len(gain)) :
            v.append(v[i] + gain[i])

        v.sort()
        
        return v[len(v) - 1]