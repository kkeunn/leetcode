class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        srsc_color = image[sr][sc]
        
        def dfs(i, j):
            # 픽셀의 색을 변경
            image[i][j] = color
            # 동서남북 탐색
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                # x와 y가 범위 안에 있고 (sr, sc)에서의 색과 같다면
                if 0 <= x < m and 0 <= y < n and  image[x][y] == srsc_color:
                    # 재귀 호출
                    dfs(x, y)
        
        if srsc_color != color:
            dfs(sr, sc)
        
        return image
            