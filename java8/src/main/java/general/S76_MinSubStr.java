package general;
import java.util.*;
/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
        Example:
        Input: S = "ADOBECODEBANC", T = "ABC"
        Output: "BANC"

        Note:
        If there is no such window in S that covers all characters in T, return the empty string "".
        If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
*/
public class S76_MinSubStr {

    public String minWindow(String s, String t) {
        int ei = 0;
        int resultStart = -1;
        int resultEnd = -1;
        Map<Character, Integer> csQueue  = new HashMap<>();
        Set<Character> dSet = new HashSet<>();

        LinkedList<Integer> queue = new LinkedList<>();
        t.chars().mapToObj(i->Character.valueOf((char)i)).forEach(c->{
            dSet.add(c);
            int cnt = csQueue.get(c) == null ? 1 : csQueue.get(c) + 1;
            csQueue.put(c, cnt);
        });

        while(ei < s.length()) {
            Character c = Character.valueOf(s.charAt(ei));
            if(!dSet.isEmpty()) {
                if(csQueue.keySet().contains(c)) {
                    int ccount = csQueue.get(c)-1;
                    csQueue.put(c, ccount);
                    queue.add(ei);
                    if(ccount == 0) {
                        dSet.remove(c);
                    }
                }
                ei++;
            }
            if(dSet.isEmpty()) {
                //calc
                while(!queue.isEmpty() && dSet.isEmpty()) {
                    int start = queue.getFirst();
                    int end = queue.getLast();
                    if(resultStart == -1 && resultEnd == -1 || ((end-start) < (resultEnd - resultStart))) {
                        resultStart = start;
                        resultEnd = end;
                    }
                    Character popedC = s.charAt(queue.removeFirst());
                    int ccount = csQueue.get(popedC) + 1;
                    csQueue.put(popedC, ccount);
                    if (ccount == 1) {
                        dSet.add(popedC);
                    }
                }
            }
        }

        return resultStart == -1 ? "" : s.substring(resultStart, resultEnd+1);
    }
}
