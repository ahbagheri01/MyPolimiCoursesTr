import unittest

from evaluation.src.metrics import edit_counts, normalize, normalized_distance
from evaluation.src.pipeline import common_segments, medoid


class MetricsTests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(normalize("Hello, WORLD! It’s 42."), ["hello", "world", "it's", "42"])

    def test_known_edit_counts(self):
        edits = edit_counts("a b c".split(), "a x c d".split())
        self.assertEqual((edits.substitutions, edits.insertions, edits.deletions), (1, 1, 0))
        self.assertEqual(normalized_distance("a b c".split(), "a x c d".split()), 0.5)

    def test_medoid(self):
        name, words = medoid({"a": "one two".split(), "b": "one two".split(), "c": "one too".split()})
        self.assertIn(name, {"a", "b"})
        self.assertEqual(words, ["one", "two"])

    def test_five_minute_line_splits_into_ten_windows(self):
        segments = common_segments(" ".join(str(i) for i in range(100)), 300, 300)
        self.assertEqual(len(segments), 10)
        self.assertTrue(all(len(segment) == 10 for segment in segments))


if __name__ == "__main__":
    unittest.main()
