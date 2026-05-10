function average(numbers) {
    // NaN yoxlaması əlavə edildi
    const valid = numbers.filter(n => typeof n === "number" && !Number.isNaN(n));
    if (valid.length === 0) return 0;
    // Reduce üçün 0 başlanğıc dəyəri qoyuldu
    const sum = valid.reduce((acc, n) => acc + n, 0);
    return parseFloat((sum / valid.length).toFixed(2));
}