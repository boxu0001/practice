package general;

import org.junit.Test;

import static org.junit.Assert.*;

public class S75_CountingSortTest {

    @Test
    public void test1() {
        S75_CountingSort s = new S75_CountingSort();

        int[] t = new int[]{1,2,0};
        s.sortColors2(t);
        assertArrayEquals(new int[]{0,1,2}, t);

        int[] t1 = new int[]{2,0,2,1,1,0};
        s.sortColors2(t1);
        assertArrayEquals(new int[]{0,0,1,1,2,2}, t1);

        int[] t2 = new int[]{2,0};
        s.sortColors2(t2);
        assertArrayEquals(new int[]{0,2}, t2);
    }

}