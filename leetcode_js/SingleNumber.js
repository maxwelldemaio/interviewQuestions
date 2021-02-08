/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let mySet = new Set();
    for (let num of nums) {
        if (mySet.has(num)) {
            mySet.delete(num);
        } else {
            mySet.add(num);
        }
    }
    return Array.from(mySet)[0];
};