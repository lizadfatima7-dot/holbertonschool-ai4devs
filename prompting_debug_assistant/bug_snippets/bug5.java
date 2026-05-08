import java.util.HashMap;
import java.util.Map;

/**
 * Intended: Count how many times each word appears in a sentence,
 *           then print the word with the highest count.
 * Bug Type: Runtime NullPointerException + logical error in max-finding
 */
public class WordCounter {

    public static Map<String, Integer> countWords(String sentence) {
        Map<String, Integer> counts = new HashMap<>();
        // BUG: no null check — throws NullPointerException if sentence is null
        String[] words = sentence.toLowerCase().split(" ");

        for (String word : words) {
            // BUG: should use counts.getOrDefault(word, 0)
            counts.put(word, counts.get(word) + 1);  // NullPointerException on first occurrence
        }
        return counts;
    }

    public static String mostFrequent(Map<String, Integer> counts) {
        String best = null;
        int max = 0;
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            // BUG: >= should be > to keep first occurrence on tie, but also
            //      if all counts are equal it returns the last key (arbitrary)
            if (entry.getValue() >= max) {
                max = entry.getValue();
                best = entry.getKey();
            }
        }
        return best;   // BUG: returns null if counts is empty — no guard
    }

    public static void main(String[] args) {
        String sentence = "the cat sat on the mat the cat";
        Map<String, Integer> result = countWords(sentence);
        System.out.println("Most frequent: " + mostFrequent(result));
        // Expected: "the" (appears 3 times)

        // Crash demo:
        countWords(null);   // NullPointerException
    }
}
