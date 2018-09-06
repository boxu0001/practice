package greedy;

import org.junit.Test;

import static org.junit.Assert.*;

public class S_flowersTest {

    @Test
    public void test1() {
        S_flowers sf = new S_flowers();
        assertEquals(13, sf.getMinimumCost(3, new int[]{2, 5, 6}));
        assertEquals(15, sf.getMinimumCost(2, new int[]{2, 5, 6}));
        assertEquals(29, sf.getMinimumCost(3, new int[]{1,3,5,7,9}));
    }
}