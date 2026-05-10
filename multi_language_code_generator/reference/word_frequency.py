import re
import json
from collections import Counter
from typing import Union


class WordFrequencyAnalyzer:
    """Reference implementation of the Word Frequency Analyzer algorithm."""

    def analyze(self, text: str, top_n: int = 5) -> dict:
        """
        Analyze word frequencies in a given text.

        Args:
            text: Input text string to analyze.
            top_n: Number of top frequent words to return.

        Returns:
            A dictionary with total_words, unique_words, top_n,
            average_word_length, and longest_word.
        """
        words = self._extract_words(text)

        if not words:
            return {
                "total_words": 0,
                "unique_words": 0,
                "top_n": [],
                "average_word_length": 0.00,
                "longest_word": ""
            }

        total_words = len(words)
        word_counts = Counter(words)
        unique_words = len(word_counts)
        top_n_words = [
            {"word": word, "count": count}
            for word, count in word_counts.most_common(top_n)
        ]
        average_word_length = round(
            sum(len(w) for w in words) / total_words, 2
        )
        longest_word = max(words, key=len)

        return {
            "total_words": total_words,
            "unique_words": unique_words,
            "top_n": top_n_words,
            "average_word_length": average_word_length,
            "longest_word": longest_word
        }

    def analyze_file(self, file_path: str, top_n: int = 5) -> dict:
        """
        Analyze word frequencies from a text file.

        Args:
            file_path: Path to the input text file.
            top_n: Number of top frequent words to return.

        Returns:
            A dictionary with analysis results.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            return self.analyze(text, top_n)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

    def _extract_words(self, text: str) -> list:
        """
        Extract normalized words from text by stripping punctuation
        and converting to lowercase.

        Args:
            text: Raw input text.

        Returns:
            List of cleaned lowercase words.
        """
        raw_words = text.split()
        words = []
        for word in raw_words:
            cleaned = re.sub(r'[^\w]', '', word).lower()
            if cleaned:
                words.append(cleaned)
        return words

    def to_json(self, result: dict) -> str:
        """Convert analysis result to JSON string."""
        return json.dumps(result, indent=2)