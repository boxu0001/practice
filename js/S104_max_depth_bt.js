// Given a binary tree, find its maximum depth.

// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

// Note: A leaf is a node with no children.

// Example:

// Given binary tree [3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7

// return its depth = 3.

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    let s = [];
    let r = 0;
    if(root !== null) {
        s.push(root);
        r = 1;
    }
    let visited = new TreeNode(0);
    while(s.length > 0) {
        let curr = s[s.length-1];
        if(visited === curr.right || (visited === curr.left && curr.right ===null) || (curr.left === null && curr.right === null)) {
            visited = s.pop();
            continue;
        } if(visited === curr.left && curr.right !==null) {
            s.push(curr.right);
        } else if(curr.left !== null) {
            s.push(curr.left);
        } else{
            s.push(curr.right);
        } 
        r = Math.max(r, s.length);
    }
    return r;
};

var maxDepth2 = function(root) {
    return findDepth(root, 0)
};
function findDepth(root, depth){
    if(!root){
        return depth
    }
    let leftDepth = findDepth(root.left, depth + 1);
    let rightDepth = findDepth(root.right, depth + 1);
    return Math.max(leftDepth, rightDepth);
}


let r = new TreeNode(5);
r.left = new TreeNode(2);
r.right = new TreeNode(8);
r.left.left = new TreeNode(1);
r.right.left = new TreeNode(6);
r.right.right = new TreeNode(9);

console.log(maxDepth(r));
