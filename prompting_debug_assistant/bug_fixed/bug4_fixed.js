async function getUserNames(url) {
    const response = await fetch(url);
    const data = await response.json();
    const names = data.map(user => user.name.toUpperCase());
    return names;
}

const result = getUserNames("https://jsonplaceholder.typicode.com/users");
console.log("Names:", result);