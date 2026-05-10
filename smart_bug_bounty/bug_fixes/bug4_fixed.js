async function getUserNames(url) {
    // Promise-lərin həll olunması üçün await əlavə edildi
    const response = await fetch(url);
    const data = await response.json();
    return data.map(user => user.name.toUpperCase());
}