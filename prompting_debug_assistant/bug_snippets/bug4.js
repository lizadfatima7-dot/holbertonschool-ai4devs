/**
 * Intended: Fetch a list of user objects from a URL and return
 *           an array of their names in uppercase.
 * Bug Type: Misuse of async/await (missing await, unhandled promise)
 */

async function getUserNames(url) {
    const response = fetch(url);          // BUG: missing await — response is a Promise, not a Response
    const data = response.json();         // BUG: calling .json() on a Promise object → TypeError
    
    // BUG: data is still a Promise here, .map will fail
    const names = data.map(user => user.name.toUpperCase());
    return names;
}

// BUG: result is a Promise but treated as a plain value
const result = getUserNames("https://jsonplaceholder.typicode.com/users");
console.log("Names:", result);   // Prints: Names: Promise { <pending> }

// Correct call would be:
// getUserNames("...").then(names => console.log(names)).catch(console.error);
