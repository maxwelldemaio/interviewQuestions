/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    romMap = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };

    let intSum = 0;
    for (let i = 0; i < s.length; i++) {
        let currInt = romMap[s.charAt(i)];
        let nextInt = romMap[s.charAt(i + 1)];

        // So long as we're in bounds
        if (nextInt) {
            if (currInt >= nextInt) {
                // When comparing two roman numerals, current is >= next
                intSum += currInt;
            } else {
                // Add the next integer minus the current integer
                // Skip the next two positions (already taken two into account)
                // Shifting by one, i gets incremented in the for-loop (so twice)
                intSum += nextInt - currInt;
                i++;
            }
        } else {
            // We reached our final roman numeral
            intSum += currInt;
        }
        
    }
    return intSum;
};

console.log(romanToInt("IV"));
console.log(romanToInt("MCMXCVI"));