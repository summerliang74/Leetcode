class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lst=[]
        fen=p[0]
        news=s.split(fen)
        for i in news:
            if 