/* 15 July 2018 -> Domlur bangalore
 * Problem statement:
 * Given a 2D matrix of 1s and 0s find the number of connected 1s
 *
 * Answer for the below matrix: 3
 * */

public class MatrixTraverse {

    static int matrix[][] = new int[][]{
            {1, 0, 0, 1, 0},
            {1, 1, 0, 0, 0},
            {1, 0, 0, 0, 0},
            {0, 0, 1, 0, 0}
    };

    static int numberOfConnections = 0;

    public static void main(String args[]) {
        System.out.println("Number of connected 1s: " + getNumberOfConnectedComponents());
    }

    static int getNumberOfConnectedComponents() {

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {

                if (matrix[i][j] == 1) {
                    numberOfConnections++;
                    travel(i, j);
                }
            }
        }

        return numberOfConnections;
    }

    static void travel(int x, int y) {
        try {
            if (matrix[x][y] == null) {   // null -> will produce ArrayIndexOutOfBoundsException
                return;

            } else if (matrix[x][y] != 1) {
                return;

            } else {    // matrix[0][0] == 1
                matrix[x][y] = -1;      // changing so that when we revisit this index we do not consider it again for traversal

                travel(x, y - 1);
                travel(x + 1, y - 1);
                travel(x + 1, y);
                travel(x + 1, y + 1);
                travel(x, y + 1);
                travel(x - 1, y + 1);
                travel(x - 1, y);
                travel(x - 1, y - 1);
            }

        } catch (ArrayIndexOutOfBoundsException e) {
            return;
        }
    }
}
