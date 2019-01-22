// Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

// For example:
// Given binary tree [3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7

// return its zigzag level order traversal as:

// [
//   [3],
//   [20,9],
//   [15,7]
// ]


function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    let cq = [];
    if(root !== null) {
        cq.push(root);
    }
    let level = 0;
    let result = [];
    while(cq.length > 0) {
        let nq = [];
        let ri = [];
        cq.forEach(function(ele) {
            if(level % 2 === 0) {
                ri.push(ele.val);
            } else {
                ri.unshift(ele.val);
            }
            if(ele.left !== null) {
                nq.push(ele.left);
            }
            if(ele.right !== null) {
                nq.push(ele.right);
            }   
        });
        result.push(ri);
        cq = nq;
        level++;
    }
    return result;
};

let r = new TreeNode(5);
r.left = new TreeNode(2);
r.right = new TreeNode(8);
r.left.left = new TreeNode(1);
r.right.left = new TreeNode(6);
r.right.right = new TreeNode(9);

console.log(zigzagLevelOrder(r));

console.log(zigzagLevelOrder(null));
