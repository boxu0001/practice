// Given preorder and inorder traversal of a tree, construct the binary tree.
// Note:
// You may assume that duplicates do not exist in the tree.
// For example, given
// preorder = [3,9,20,15,7]
// inorder = [9,3,15,20,7]
// Return the following binary tree:
//     3
//    / \
//   9  20
//     /  \
//    15   7

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    var bbt = function(ps, pe, ib, it) {
        if(ps >= pe) {
            return null;
        }
        if(pe - ps === 1) {
            return new TreeNode(preorder[ps]);
        }
        let root = new TreeNode(preorder[ps]);
        let idx = it-1;
        while(idx >= ib) {if(inorder[idx] === root.val) {break;} idx--;}
        let nofe = idx - ib;
        if(nofe >= 0) {
            root.left = bbt(ps+1, ps+1+nofe, ib, idx);
            root.right = bbt(ps+1+nofe, pe, idx+1, it);
        }
        return root;
    }

    return bbt(0, preorder.length, 0, inorder.length);
};

let preorder = [1,2];
let inorder = [1,2];

let rooot = buildTree(preorder, inorder);
console.log(rooot);
