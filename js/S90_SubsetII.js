/**
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

 *
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    var cnt = new Map();
    nums.forEach(function(v, i) {
        if(cnt.get(v) === undefined) {
            cnt.set(v, 2);  
        } else {
            cnt.set(v, cnt.get(v)+1);  
        }
    });

    var result = [];
    var total = 1;
    cnt.forEach(function(v, k) {
        total *= v;
    });
    for(var i = 0; i < total; i++) {
        var ci = [];
        var cn = i;
        cnt.forEach(function(v, k) {
            var ti = cn%v;
            cn = Math.floor(cn/v);
            for(var j = 0; j < ti; j++) {
                ci.push(k);
            }
        });
        result.push(ci);
    }
    return result;
};

var k = subsetsWithDup([0,1,1,2]);
console.log(k);
k = subsetsWithDup([1,2,2]);
