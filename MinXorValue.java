import java.util.ArrayList;
import java.util.Collections;

// Problem: https://www.interviewbit.com/problems/min-xor-value/
// Solution: Working

public class MinXorValue {

    public static void main(String[] args) {


    }

    public static int findMinXor(ArrayList<Integer> list) {

        Collections.sort(list);

        int minXor = -1;

        for (int i = 0; i < list.size() - 1; i++) {
            int currentXor = list.get(i) ^ list.get(i+1);

            if (minXor == -1 || currentXor < minXor) {
                minXor = currentXor;
            }
        }

        return minXor;
    }
}
