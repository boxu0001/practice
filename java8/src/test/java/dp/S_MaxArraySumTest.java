package dp;

import org.junit.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.*;

public class S_MaxArraySumTest {

    private int[] readArr() throws IOException {
        Stream<String> s = Files.lines(Paths.get("src/test/java/dp/S_Max_test.txt"));
        try {
            List<String> lines = s.collect(Collectors.toList());
            int[] arr = Arrays.stream(lines.get(1).split(" ")).mapToInt(Integer::parseInt).toArray();
            return arr;
        } finally {
            s.close();
        }
    }

    @Test
    public void test1() throws IOException {

        S_MaxArraySum s = new S_MaxArraySum();
        assertEquals(13, s.solution(new int[]{3,7,4,6,5}));

        assertEquals(11, s.solution(new int[]{2,1,5,8,4}));

        System.out.println(s.solution(readArr()));

    }

}