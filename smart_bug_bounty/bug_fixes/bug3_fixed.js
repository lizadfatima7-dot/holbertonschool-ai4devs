function average(numbers) {
    // NaN və digər qeyri-rəqəm dəyərləri tam süzmək üçün
    const valid = numbers.filter(n => typeof n === "number" && !Number.isNaN(n));
    if (valid.length === 0) return 0;
    // Reduce üçün başlanğıc dəyəri 0 təyin edildi
    const sum = valid.reduce((acc, n) => acc + n, 0);
    return parseFloat((sum / valid.length).toFixed(2));
}