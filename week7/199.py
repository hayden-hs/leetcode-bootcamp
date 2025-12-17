class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # 현재 깊이에서 처음 방문하는 노드라면 결과에 추가
            # (오른쪽 자식을 먼저 방문하므로, 해당 깊이의 가장 오른쪽 노드가 처음 기록됨)
            if depth == len(result):
                result.append(node.val)
            
            # 오른쪽을 먼저 방문하는 것이 핵심!
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result