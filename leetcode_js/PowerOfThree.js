function log3(val) {
    return Math.log(val) / Math.log(3);
}

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
        if (n < 1) {
                return false;
        }

        while (n % 3 == 0) {
            n /= 3;
        }

        return n == 1;  
};

console.log(isPowerOfThree(9));
console.log(isPowerOfThree(27));
console.log(isPowerOfThree(45));