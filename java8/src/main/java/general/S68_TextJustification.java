package general;

import java.util.*;
import java.util.stream.*;

/**
 * Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
 *
 * You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
 *
 * Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
 *
 * For the last line of text, it should be left justified and no extra space is inserted between words.
 *
 * Note:
 *
 *     A word is defined as a character sequence consisting of non-space characters only.
 *     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
 *     The input array words contains at least one word.
 *
 *   Example 1:
 *
 * Input:
 * words = ["This", "is", "an", "example", "of", "text", "justification."]
 * maxWidth = 16
 * Output:
 * [
 *    "This    is    an",
 *    "example  of text",
 *    "justification.  "
 * ]
 *
 * Example 2:
 *
 * Input:
 * words = ["What","must","be","acknowledgment","shall","be"]
 * maxWidth = 16
 * Output:
 * [
 *   "What   must   be",
 *   "acknowledgment  ",
 *   "shall be        "
 * ]
 * Explanation: Note that the last line is "shall be    " instead of "shall     be",
 *              because the last line must be left-justified instead of fully-justified.
 *              Note that the second line is also left-justified becase it contains only one word.
 *
 *
 * Example 3:
 *
 * Input:
 * words = ["Science","is","what","we","understand","well","enough","to","explain",
 *          "to","a","computer.","Art","is","everything","else","we","do"]
 * maxWidth = 20
 * Output:
 * [
 *   "Science  is  what we",
 *   "understand      well",
 *   "enough to explain to",
 *   "a  computer.  Art is",
 *   "everything  else  we",
 *   "do                  "
 * ]
 */
public class S68_TextJustification {

    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();

        List<String> currentLine = new ArrayList<>();
        int currentRemainingWidth = maxWidth;
        for(int i = 0; i < words.length; i++) {
            if(currentLine.isEmpty()) {
                currentRemainingWidth -= words[i].length();
                currentLine.add(words[i]);
            } else if(currentRemainingWidth - 1 - words[i].length() >=0) {
                currentRemainingWidth -= words[i].length()+1;
                currentLine.add(words[i]);
            } else {
                //compose new line
                StringBuilder sb = new StringBuilder();
                if(currentLine.size() == 1) {
                    sb.append(currentLine.get(0));
                    IntStream.range(0, currentRemainingWidth).forEach(xi->sb.append(" "));
                    result.add(sb.toString());
                } else {
                    int n1 = currentRemainingWidth / (currentLine.size() - 1) + 1;
                    int n2 = currentRemainingWidth % (currentLine.size() - 1);
                    StringBuilder spaceBuilder = new StringBuilder();
                    IntStream.range(0, n1).forEach(x -> spaceBuilder.append(" "));
                    String n1Spc = spaceBuilder.toString();
                    spaceBuilder.append(" ");
                    String n2Spc = spaceBuilder.toString();

                    IntStream.range(0, n2).forEach(xi->{sb.append(currentLine.get(xi));sb.append(n2Spc);});
                    IntStream.range(n2, currentLine.size()).forEach(xi->{sb.append(currentLine.get(xi)); if(xi < currentLine.size()-1) { sb.append(n1Spc); }});
                    result.add(sb.toString());
                }

                //reset currentLine
                currentLine.clear();
                currentLine.add(words[i]);
                currentRemainingWidth = maxWidth - words[i].length();
            }
        }

        if(!currentLine.isEmpty()) {
            StringBuilder sb = new StringBuilder(currentLine.stream().collect(Collectors.joining(" ")));
            IntStream.range(0, currentRemainingWidth).forEach(i->sb.append(" "));
            result.add(sb.toString());
        }
        return result;
    }

}
