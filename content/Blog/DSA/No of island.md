```
import java.util.*;

public class GfG {

    static boolean isSafe(char[][] M, int r, int c, boolean[][] visited) {
        int ROW = M.length;
        int COL = M[0].length;
        return r >= 0 && r < ROW && c >= 0 && c < COL && M[r][c] == '1' && !visited[r][c];
    }

    static void DFS(char[][] M, int r, int c, boolean[][] visited) {
        int[] rNbr = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] cNbr = { -1, 0, 1, -1, 1, -1, 0, 1 };
        visited[r][c] = true;
        for (int k = 0; k < 8; ++k) {
            int newR = r + rNbr[k];
            int newC = c + cNbr[k];
            if (isSafe(M, newR, newC, visited)) {
                DFS(M, newR, newC, visited);
            }
        }
    }

    static int countIslands(char[][] M) {
        int ROW = M.length;
        int COL = M[0].length;
        boolean[][] visited = new boolean[ROW][COL];
        int count = 0;
        for (int r = 0; r < ROW; ++r) {
            for (int c = 0; c < COL; ++c) {
                if (M[r][c] == '1' && !visited[r][c]) {
                    DFS(M, r, c, visited);
                    ++count;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        sc.nextLine(); 
        char[][] M = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < cols; j++) {
                M[i][j] = line.charAt(j);
            }
        }
        System.out.println(countIslands(M));
    }
}

```
