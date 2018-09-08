package general;

import org.junit.Test;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static org.junit.Assert.*;

public class S68_TextJustificationTest {

    private S68_TextJustification s = new S68_TextJustification();

    @Test
    public void test1() {
        String[] arr1 = new String[]{"This", "is", "an", "example", "of", "text", "justification."};
        List<String> r1 = s.fullJustify(arr1, 16);

        assertEquals("This    is    an", r1.get(0));
        assertEquals("example  of text", r1.get(1));
        assertEquals("justification.  ", r1.get(2));

    }


    @Test
    public void test2() {
        String[] arr1 = new String[]{"What","must","be","acknowledgment","shall","be"};
        List<String> r1 = s.fullJustify(arr1, 16);

        assertEquals("What   must   be", r1.get(0));
        assertEquals("acknowledgment  ", r1.get(1));
        assertEquals("shall be        ", r1.get(2));

    }


    @Test
    public void test3() {
        String[] arr1 = new String[]{"Science","is","what","we","understand","well","enough","to","explain",
                "to","a","computer.","Art","is","everything","else","we","do"};
        List<String> r1 = s.fullJustify(arr1, 20);

        assertEquals("Science  is  what we", r1.get(0));
        assertEquals("understand      well", r1.get(1));
        assertEquals("enough to explain to", r1.get(2));
        assertEquals("a  computer.  Art is", r1.get(3));
        assertEquals("everything  else  we", r1.get(4));
    }

    @Test
    public void test4() {
        String[] arr1 = new String[]{"Science", "1234567890123456789 "};
        List<String> r1 = s.fullJustify(arr1, 20);

        assertEquals("Science             ", r1.get(0));
        assertEquals("1234567890123456789 ", r1.get(1));
    }

}