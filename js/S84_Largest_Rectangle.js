/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    var max = 0;
    var stack = [];
    heights.unshift(0);
    heights.push(0);
    for(var i = 0; i < heights.length; i++) {
        while(stack.length > 0 && heights[i] < heights[stack[stack.length-1]]) {
            var pi = stack.pop();
            max = Math.max((i-1-stack[stack.length-1])*heights[pi], max);
        }
        stack.push(i);
    }
    return max;
};