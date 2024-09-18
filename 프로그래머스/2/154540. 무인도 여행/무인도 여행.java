import java.util.*;

class Solution {
    int[] dx = {-1, 1, 0, 0};  // 상하좌우 이동을 위한 배열
    int[] dy = {0, 0, -1, 1};
    int m, n;  // 지도의 크기
    
    public int[] solution(String[] maps) {
        m = maps.length;
        n = maps[0].length();
        boolean[][] visited = new boolean[m][n];
        List<Integer> islands = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && maps[i].charAt(j) != 'X') {
                    islands.add(dfs(maps, visited, i, j));
                }
            }
        }
        
        if (islands.isEmpty()) {
            return new int[]{-1};
        }
        
        Collections.sort(islands);
        return islands.stream().mapToInt(i -> i).toArray();
    }
    
    private int dfs(String[] maps, boolean[][] visited, int x, int y) {
        visited[x][y] = true;
        int sum = maps[x].charAt(y) - '0';
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                sum += dfs(maps, visited, nx, ny);
            }
        }
        
        return sum;
    }
}