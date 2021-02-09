/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        // Normal case (no carry over)
        // Just increment the last element in the array by 1
        if (digits[i] < 9) {
            digits[i] = digits[i] + 1;
            return digits;
        } else {
            digits[i] = 0;

        }
    }
    
    // Edge case where all elements are 9s
    digits.unshift(1)
    return digits;
};

// Tests
console.log(plusOne([1,2,3]));
console.log(plusOne([0, 0, 0]));
console.log(plusOne([1, 2, 9]));