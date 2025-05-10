import unittest
from Sentimentanal import analyze_sentiment

# Python

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        result = analyze_sentiment("I love this product, it is amazing!")
        self.assertEqual(result, "positive")

    def test_negative_sentiment(self):
        result = analyze_sentiment("I hate this product, it is terrible!")
        self.assertEqual(result, "negative")

    def test_neutral_sentiment(self):
        result = analyze_sentiment("This product is okay, nothing special.")#will fail because model isn't trained on neutral
        self.assertEqual(result, "neutral")

    def test_not_handling(self):
        result = analyze_sentiment("This product is not good.")
        self.assertEqual(result, "negative")  # Expected to be negative

if __name__ == "__main__":
    unittest.main()