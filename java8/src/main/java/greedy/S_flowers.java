package greedy;

import java.util.Arrays;
import java.util.stream.IntStream;

public class S_flowers {

    // Complete the getMinimumCost function below.
    int getMinimumCost(int k, int[] c) {

        Arrays.sort(c);

        int t = c.length/k;
        int m = c.length%k;

        int r = 0;
        if(m > 0) {
            r += (t+1) * Arrays.stream(c,0,m).sum();
        }

        for(int i = 0; i< t; i++) {
            r += (t-i) * Arrays.stream(c,m+i*k, m+i*k+k).sum();
        }

        return r;
    }
}
