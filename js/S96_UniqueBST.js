/**
 * Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    var f = [1, 1];

    for(var i = 2; i <= n; i++) {
        var fi = 0;
        var halfi = i >> 1;
        for(var k=0; k < halfi; k++) {
            fi+=f[k]*f[i-k-1]*2;
        }
        if(i%2 == 1) {
            fi+=f[halfi]*f[i-1-halfi];
        }
        f.push(fi);
    }
    return f[n];
};

// console.log(numTrees(3));
// console.log(numTrees(4));
console.log(numTrees(7));