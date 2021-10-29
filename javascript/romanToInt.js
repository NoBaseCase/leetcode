/**
 * For example, 2 is written as II in Roman numeral, just two one's added together. 
 * 12 is written as XII, which is simply X + II. 
 * The number 27 is written as XXVII, which is XX + V + II.
 * @param {string} s
 * @return {number}
 */
 var romanToInt = function(s) {
    //  function output
    let output = 0;

    // create a map to index roman keys with values
    const map = new Map();
    map.set('I', 1)
    map.set('V', 5)
    map.set('X', 10)
    map.set('L', 50)
    map.set('C', 100)
    map.set('D', 500)
    map.set('M', 1000)
    map.set('IV', 4)
    map.set('IX', 9)
    map.set('XL', 40)
    map.set('XC', 90)
    map.set('CD', 400)
    map.set('CM', 900)

    // iterate through the string of roman numerals
    for (let current = 0; current < s.length; current++) {
        // if there exists a map key with multiple roman numerals, add to output and increment by 2
        if (map.has(s[current] + s[current+1])) {
            output += map.get(s[current] + s[current+1])
            current++;
        }
        // if not, just get roman numeral value and add to output
        else {
            output += map.get(s[current])
        }        
    }
    return output
};

console.log(romanToInt('MCMXCIV'))