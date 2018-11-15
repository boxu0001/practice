// Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

// Example 1:

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true

// Example 2:

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false

/**
 * Breath Search First implementation
 * 
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    //the queue
    var q = [[-1,-1]];
    while(q.length > 0) {
        var i = q[0][0];
        var j = q[0][1];
        if(i === s1.length -1 && j === s2.length -1 && i+j+2 === s3.length) {
            return true;
        }
        var li = q[q.length-1][0];
        var lj = q[q.length-1][1];
        if(i+j+2 < s3.length && i+1 < s1.length && s1[i+1] === s3[i+j+2] && (i+1 !== li || j !== lj)) {
            q.push([i+1, j]);
        }
        if(i+j+2 < s3.length && j+1 < s2.length && s2[j+1] === s3[i+j+2]) {
            q.push([i, j+1]);
        }
        q.splice(0, 1);
    }
    return false;
};

var f=isInterleave;
// console.log(f("", "", "a"));
console.log(f("aabcc", "dbbca", "aadbbcbcacd"));
// console.log(f("aabcc", "dbbca", "aadbbbaccc"));

