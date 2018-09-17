package general;

import java.util.Arrays;
import java.util.stream.IntStream;

/*
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Note: You are not suppose to use the library's sort function for this problem.

        Example:

        Input: [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

        Follow up:

        A rather straight forward solution is a two-pass algorithm using counting sort.
        First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
        Could you come up with a one-pass algorithm using only constant space?
*/
public class S75_CountingSort {

    public void sortColors(int[] nums) {
        int[] c = new int[]{0, 0};
        Arrays.stream(nums).forEach(i->{
            if(i == 1) {
                c[0]++;
            } else if(i == 2) {
                c[1]++;
            }
        });
        int c0 = nums.length - c[0] - c[1];
        int c1 = c0+c[0];
        IntStream.range(0, c0).forEach(i->nums[i]=0);
        IntStream.range(c0, c1).forEach(i->nums[i]=1);
        IntStream.range(c1, nums.length).forEach(i->nums[i]=2);
    }

    public void sortColors2(int[] nums) {
        int next0 = 0;
        int next2 = nums.length - 1;
        int i = 0;

        while(i <= next2) {
            if(nums[i] == 0) {
                int t = nums[next0];
                nums[next0++] = nums[i];
                nums[i] = t;
            } else if(nums[i] == 2) {
                int t = nums[next2];
                nums[next2--] = nums[i];
                nums[i] = t;
            }
            if(nums[i] == 1 || next0 > i){
                i++;
            }
        }
    }
}
