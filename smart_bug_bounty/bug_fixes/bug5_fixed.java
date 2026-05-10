import java.util.HashMap;
import java.util.Map;

public class WordCounter {
    public static Map<String, Integer> countWords(String sentence) {
        if (sentence == null) return new HashMap<>();
        Map<String, Integer> counts = new HashMap<>();
        String[] words = sentence.toLowerCase().split(" ");
        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0) + 1);
        }
        return counts;
    }
}