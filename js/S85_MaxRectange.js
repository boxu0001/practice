/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
	var max = 0;
	var heights = undefined;
	for(var r = 0; r < matrix.length; r++) {
		if(heights === undefined) {
			//preset height[0], height[end]=0, real heights start from index 1, end end index n.
			heights = new Array(matrix[r].length+2);
			heights[0] = 0;
			heights[heights.length-1] = 0;
		}
		for(var i = 0; i < matrix[r].length; i++) {
			var preh = heights[i+1] === undefined ? 0 : heights[i+1];
			heights[i+1] = matrix[r][i] === "1" ? preh + 1 : 0;
		}
		var stack=[];
		for(var i = 0; i < heights.length; i++) {
			while(stack.length > 0 && heights[i] < heights[stack[stack.length-1]]) {
				var pi = stack.pop();
				max = Math.max((i-1-stack[stack.length-1])*heights[pi], max);
			}
			stack.push(i);
		}

	}
	return max;
};