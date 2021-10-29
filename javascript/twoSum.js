/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    //  get length of number list for readability
    const length = nums.length;
    // function output
    output = []
    // traverse through the numberlist and stop and second to last number
    // this is necessary because our traveser variable will alwasy be ahead by 1
    for (let current = 0; current < length - 1; current++) {
        // traverse starting at the current index + 1
        for (let traverser = current + 1; traverser < length; traverser++) {
            // if we get a match, add indexes to output and return 
            if (nums[current] + nums[traverser] == target) {
                output.push(current);
                output.push(traverser);
                return output
            }
        }
    }
    return output
};

console.log(twoSum([1,2,3], 4))