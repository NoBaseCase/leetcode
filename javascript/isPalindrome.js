/**
 * Given an integer x, return true if x is palindrome integer.
 * An integer is a palindrome when it reads the same backward as forward. 
 * For example, 121 is palindrome while 123 is not.
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function (x) {
    //  convert number into string
    const y = x.toString();
    // get length of string for readability
    const length = y.length;
    // funciton output
    let output = true;

    // loop through the string
    for (let index = 0; index < length; index++) {
        // get front and rear positions for read
        let front = index;
        let back = length - 1 - index;
        // if back and front are equal to each other (odd numbered string)
        // or back is great than front (even numbered string), break the loop and break
        if (back <= front) {
            break;
        } else {
            // if the front does not equal the backside, set to false and break
            if (y[front] != y[back]) {
                output = false;
                break;
            }
        }
    }
    return output;
};

console.log(isPalindrome(010101));
