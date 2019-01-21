// Input: 3
// Output:
// [
//   [1,null,3,2],
//   [3,2,null,1],
//   [3,1,null,null,2],
//   [2,1,3],
//   [1,null,2,null,3]
// ]
// Explanation:
// The above output corresponds to the 5 unique BST's shown below:

//    1         3     3      2      1
//     \       /     /      / \      \
//      3     2     1      1   3      2
//     /     /       \                 \
//    2     1         2                 3


function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    if(n === 0) {
        return [];
    }
    var genTree = function(s, e) {
        if(s > e) {
            return [null];
        } else {
            let ri = [];
            for(let i = s; i <= e; i++ ) {
                let lft = genTree(s, i-1);
                let rgt = genTree(i+1, e);
                lft.forEach(function(leftEle) {
                    rgt.forEach(function(rightEle) {
                        let nk = new TreeNode(i);
                        nk.left = leftEle;
                        nk.right = rightEle;
                        ri.push(nk);
                    });
                });
            }
            return ri;
        }
    }
    return genTree(1, n);
};

let t3 = generateTrees(3);

console.log(t3);
