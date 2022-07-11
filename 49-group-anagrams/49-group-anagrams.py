class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = {}
        for str in strs:
            str_anagrams = "".join(sorted(str))
            if str_anagrams in anagrams_dict.keys():
                anagrams_dict[str_anagrams].append(str)
            else:
                anagrams_dict[str_anagrams] = [str]
                
        return anagrams_dict.values()