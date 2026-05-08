/**
 * Intended: Accept an array of numbers, filter out non-numbers,
 *           then return their average rounded to 2 decimal places.
 * Bug Type: Runtime exception + data type misuse
 */

function average(numbers) {
    // BUG: filter keeps NaN values because typeof NaN === "number"
    const valid = numbers.filter(n => typeof n === "number");

    // BUG: If valid is empty this returns NaN, not 0 or an error message
    const sum = valid.reduce((acc, n) => acc + n);  // BUG: no initial value — crashes on empty array

    // BUG: toFixed returns a STRING, then the caller may do arithmetic on it
    return (sum / valid.length).toFixed(2);
}

console.log(average([1, 2, 3, 4, 5]));          // Expected: "3.00"
console.log(average([10, "hello", null, 20]));   // Expected: "15.00", Got: wrong due to NaN
console.log(average([]));                         // Expected: 0 or error, Crashes
