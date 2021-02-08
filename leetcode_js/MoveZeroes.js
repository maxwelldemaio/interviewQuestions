/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let anchor = 0;
    for (let traverse = 0; traverse < nums.length; traverse++) {
        if (nums[traverse] != 0) {
            let temp = nums[traverse];
            nums[traverse] = nums[anchor];
            nums[anchor] = temp;

            anchor++;
        }
    }
};

// Tests
console.log(moveZeroes([0,1,0,3,12]));