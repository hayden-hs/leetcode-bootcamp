from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # 1. 초기 상태 설정: 썩은 오렌지는 큐에 넣고, 싱싱한 오렌지는 개수를 셉니다.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # 싱싱한 오렌지가 처음부터 없다면 바로 0분 반환
        if fresh_count == 0:
            return 0
            
        # 2. BFS 시작
        # 4방향 탐색을 위한 방향 벡터 (상, 하, 좌, 우)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh_count > 0:
            minutes += 1
            # 현재 분(minute)에 썩을 수 있는 오렌지들만 처리 (레벨 단위 탐색)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # 격자 범위 내에 있고 싱싱한 오렌지라면?
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # 썩게 만듦
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        # 3. 모든 싱싱한 오렌지가 썩었는지 확인
        return minutes if fresh_count == 0 else -1