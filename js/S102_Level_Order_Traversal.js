
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    let currq = [];
    if (root !== null && root !== undefined) {
        currq.push(root);
    }
    let nextq = [];
    let result = [];
    let curRsl = [];
    while (currq.length > 0 || nextq.length > 0) {
        if (currq.length > 0) {
            let top = currq.splice(0, 1)[0]
            curRsl.push(top.val);
            if (top.left !== null && top.left !== undefined) {
                nextq.push(top.left);
            }
            if (top.right !== null && top.right !== undefined) {
                nextq.push(top.right);
            }
        } else {
            result.push(curRsl);
            curRsl = [];

            currq = nextq;
            nextq = [];
        }
    }
    if (curRsl.length > 0) {
        result.push(curRsl);
    }
    return result;
};


var levelOrder2 = function (root) {
    var res = [];
    function travel(node, depth) {
        if (!node) return;
        if (res[depth]) {
            res[depth].push(node.val);
        } else {
            res[depth] = [node.val];
        }
        travel(node.left, depth + 1);
        travel(node.right, depth + 1);
    }
    travel(root, 0);
    return res;
};

let r = new TreeNode(5);
r.left = new TreeNode(2);
r.right = new TreeNode(8);
r.left.left = new TreeNode(1);
r.right.left = new TreeNode(6);
r.right.right = new TreeNode(9);

console.log(levelOrder(r));


