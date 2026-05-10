async function getUserNames(url) {
    // Fetch və json() əməliyyatlarına await əlavə edildi
    const response = await fetch(url);
    const data = await response.json();
    const names = data.map(user => user.name.toUpperCase());
    return names;
}