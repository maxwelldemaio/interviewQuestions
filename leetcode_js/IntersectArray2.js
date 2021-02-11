/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {    
    myObj = {};
    result = [];

    
    if (nums1.length < nums2.length) {
        nums1,nums2 = nums2,nums1
    }
    
    // Create hashmap of nums1
    for (let num of nums1) {
        if (myObj[num] > 0) {
            // If number exists, increment
            myObj[num]++;
        } else {
            // Otherwise, add it to hashmap
            myObj[num] = 1;
        }
    }

    for (let num of nums2) {
        if (myObj[num] > 0) {
            result.push(num)
            myObj[num]--;
        }
    }

    return result;
};

// Tests
console.log(intersect([2, 2], [1,2,2,1]));
console.log(intersect([4,9,5], [9,4,9,8,4]));
