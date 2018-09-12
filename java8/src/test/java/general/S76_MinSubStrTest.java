package general;

import org.junit.Test;

import static org.junit.Assert.*;

public class S76_MinSubStrTest {

    @Test
    public void testMinWindow() {
        S76_MinSubStr s = new S76_MinSubStr();
        assertEquals("BANC", s.minWindow("ADOBECODEBANC", "ABC"));

        assertEquals("ba", s.minWindow("bba", "ba"));
    }
}