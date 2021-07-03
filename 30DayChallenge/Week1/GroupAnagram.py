class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:                
        ans = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in ans:
                temp = [i]
                ans[key] = temp
            else:
                ans[key].append(i)
        return ans.values()


        