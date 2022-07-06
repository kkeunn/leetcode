class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def dfs(i, j):
            # x와 y가 범위 안에 있지 않거나 (sr, sc)에서의 색과 같지 않다면 종료
            if i < 0 or i >= len(image) or \
                j < 0 or j >= len(image[0]) or\
                image[i][j] != srsc_color:
                    return

            image[i][j] = color
            # 동서남북 탐색
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
            
        srsc_color = image[sr][sc]
        
        if srsc_color != color:
            dfs(sr, sc)
        
        return image
            