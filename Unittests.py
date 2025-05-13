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
        result = analyze_sentiment("This product is okay, nothing special.")
        self.assertEqual(result, "neutral") #will fail because model isn't trained on neutral

    def test_not_handling(self):
        result = analyze_sentiment("This product is not good.")
        self.assertEqual(result, "negative")  

    def test_not_handling_positive(self):
        result = analyze_sentiment("This product is not bad.")
        self.assertEqual(result, "positive")  
    
    def test_double_negative(self):
        result = analyze_sentiment("This product is not not good.")
        self.assertEqual(result, "positive")  # fails on verison A

    def test_double_negative_negative(self):
        result = analyze_sentiment("This product is not not bad.")
        self.assertEqual(result, "negative")  # fails on verison A
    
    def test_long_sentence_1(self):
        result = analyze_sentiment("if you are thinking of buying this, don't buy it")
        self.assertEqual(result, "negative")  # Fails on Version B
    
    def test_long_sentence_2(self):
        result = analyze_sentiment("if you are thinking of buying this, don't")
        self.assertEqual(result, "negative")  # Fails on version A and B

if __name__ == "__main__":
    unittest.main() # a lot of these will fail depending on which version of vectoriser is used: base, not, double negative