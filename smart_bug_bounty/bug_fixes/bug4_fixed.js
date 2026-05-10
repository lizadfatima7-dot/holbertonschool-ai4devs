async function getUserNames(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data.map(user => user.name.toUpperCase());
}