// Good reference: https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // Define regex to clean string of invalid chars
    // All non word characters and underscores
    const re = /[\W_]/g;

    // Convert to lower case and apply regex
    let newStr = s.toLowerCase().replace(re, '');

    // Create a reverse version
    // Make into an array, reverse it, re-create into a string
    let reverStr = newStr.split('').reverse().join('');
    
    if (newStr === reverStr) {
        return true;
    }
    return false;
};

// Test cases
console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));
console.log(isPalindrome("never odd or even"));