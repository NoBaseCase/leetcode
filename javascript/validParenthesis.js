/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    //  create array to push symbols
    map = []
    
    if(s.length < 2) {
        return false
    } else {
        // iterate through string
        for (let index = 0; index < s.length; index++) {
            // if opening symbol detected, push to list
            if (s[index] == '(' || s[index] == '[' || s[index] == '{' ) {
                map.push(s[index])
            } else {
                // if closing symbol detected, check previous symbol in list to determin validity
                // if valid, pop off symbol from list
                if (s[index] == ')' && map[map.length-1] == '(') {
                    map.pop('(')
                } else if (s[index] == ']' && map[map.length-1] == '[' ) {
                    map.pop(']')
                } else if (s[index] == '}' && map[map.length-1] == '{' ) {
                    map.pop(']')
                } else {
                    return false;
                }
            }
        }
        // if list is empty (valid), return true
        if(map.length == 0) {
            return true
        } else {
            return false
        }
    }
};

console.log(isValid(')['))