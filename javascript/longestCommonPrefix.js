/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
    // function outpout
    let output = '';
    // base word to reference
    const firstWord = strs[0];

    // grab the lenfth of the smallest word in the list
    wordList = []
    strs.forEach(str => {
        wordList.push(str.length)
    });
    smallestWordLength = Math.min(...wordList)

    // outloop keeps track of the letter bieng check 
    for (let letter = 0; letter < smallestWordLength; letter++) {
        // inner loop keeps track of the words being checked
        for (let word = 0;  word< strs.length; word++) {
            // if there is 
            if(strs[word][letter] != firstWord[letter]) {
                return output
            }
        }
        output += firstWord[letter];
    }
    return output;
};

console.log(longestCommonPrefix(['flower', 'flow', 'floght']));
