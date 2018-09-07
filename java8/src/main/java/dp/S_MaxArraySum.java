package dp;

import java.util.Arrays;

public class S_MaxArraySum {

    public int solution(int[] array) {
        int[] f = new int[array.length];
        f[0] = array[0];
        f[1] = Math.max(array[0], array[1]);
        for(int j = 2; j < array.length; j++) {
            f[j] = Math.max(Math.max(f[j-2]+array[j], f[j-1]), array[j]);
        }
        return f[array.length-1];
    }
}
