python -c "
content = '''import java.util.HashMap;
import java.util.Map;

public class WordCounter {
    public static Map countWords(String sentence) {
        Map counts = new HashMap<>();
        String[] words = sentence.toLowerCase().split(\" \");
        for (String word : words) {
            counts.put(word, counts.get(word) + 1);
        }
        return counts;
    }

    public static String mostFrequent(Map counts) {
        String best = null;
        int max = 0;
        for (Map.Entry entry : counts.entrySet()) {
            if ((int)entry.getValue() >= max) {
                max = (int)entry.getValue();
                best = (String)entry.getKey();
            }
        }
        return best;
    }

    public static void main(String[] args) {
        String sentence = \"the cat sat on the mat the cat\";
        Map result = countWords(sentence);
        System.out.println(\"Most frequent: \" + mostFrequent(result));
        countWords(null);
    }
}
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\smart_bug_bounty\bug_snippets\bug5.java', 'w') as f:
    f.write(content)
print('Done')
"