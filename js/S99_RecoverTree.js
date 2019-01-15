
  function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
  }

/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let s = [];
    let curr = root;
    let lastO = undefined;
    let big = undefined;
    let small = undefined;
    while(s.length > 0 || curr !== null) {
        if(curr !== null) {
            s.push(curr);
            curr = curr.left;
        } else {
            let poped = s.pop();
            
            if(lastO !== undefined && lastO.val > poped.val) {
                if(big === undefined) {
                    big = lastO;
                }
                small = poped;
            }
            // console.log(poped.val);
            curr = poped.right;
            lastO = poped;
        }
    }
    if(big !== undefined && small !== undefined) {
        let temp = big.val;
        big.val = small.val;
        small.val = temp;
    }
};

let r = new TreeNode(5);
r.left = new TreeNode(9);
r.right = new TreeNode(7);
r.left.left = new TreeNode(1);
r.right.right = new TreeNode(3);

recoverTree(r);

recoverTree(r);
