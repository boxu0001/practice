'use strict'

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    var lf = new Array(heights.length);
    var max = 0;
    for(var i = 0; i < heights.length; i++) {
        if(lf[i] === undefined) {
            lf[i] = i;
        }
        var j = i+1;
        while(j < heights.length && heights[j] >= heights[i]) {
            if(heights[j] > heights[i]) {
                lf[j] = i+1;
            }
            j++;
        }
        if(j < heights.length) {
            if(lf[j] === undefined) {
                var x = i;
                while(x > lf[x]) {
                    x = lf[x];
                }
                lf[j] = x;
            }
        }
        max = Math.max(max, (j-lf[i])*heights[i]);
    }
    return max;
};

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea2 = function(heights) {
    var fleft = new Array(heights.length);
    var fright = new Array(heights.length);
    var max = 0;
    for(var i = heights.length-1; i >= 0; i--) {
        var j = i+1;
        while(j < heights.length && heights[j] >= heights[i]) {
            j+=fright[j]+1;
        }
        fright[i] = j-i-1;
    }
    for(var i = 0; i < heights.length; i++) {
        var j = i-1;
        while(j>=0 && heights[j] >= heights[i]) {
            j-=fleft[j]-1;
        }
        fleft[i] = i-j-1;
        max = Math.max(max, (fleft[i] + fright[i] + 1)*heights[i]);
    }
 
    return max;
};


console.log(largestRectangleArea2([12,11,10,9,8,7,6,5,4,3,2,1]));

