import unittest
from Sentimentanal import analyze_sentiment

# Python

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        result = analyze_sentiment("I love this product, it is amazing!")
        self.assertEqual(result, "positive") # Expected to be positive

    def test_negative_sentiment(self):
        result = analyze_sentiment("I hate this product, it is terrible!")
        self.assertEqual(result, "negative") # Expected to be negative

    def test_neutral_sentiment(self):
        result = analyze_sentiment("This product is okay, nothing special.")#will fail because model isn't trained on neutral
        self.assertEqual(result, "neutral") # Expected to be neutral

    def test_not_handling(self):
        result = analyze_sentiment("This product is not good.")
        self.assertEqual(result, "negative")  # Expected to be negative

    def test_not_handling_positive(self):
        result = analyze_sentiment("This product is not bad.")
        self.assertEqual(result, "positive")  # Expected to be positive
    
    def test_double_negative(self):
        result = analyze_sentiment("This product is not not good.")
        self.assertEqual(result, "positive")  # Expected to be positive

    def test_double_negative(self):
        result = analyze_sentiment("This product is not not bad.")
        self.assertEqual(result, "negative")  # Expected to be negative
    
    def test_long_sentence_1(self):
        result = analyze_sentiment("if you are thinking of buying this, don't buy it")
        self.assertEqual(result, "negative")  # Expected to be negative
    
    def test_long_sentence_2(self):
        result = analyze_sentiment("if you are thinking of buying this, don't")
        self.assertEqual(result, "negative")  # Expected to be negative

if __name__ == "__main__":
    unittest.main()