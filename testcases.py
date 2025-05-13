import unittest
from Sentimentanal import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_1(self):
        result = analyze_sentiment("Oh fantastic, another bug. Just what I needed.")
        self.assertEqual(result, "negative") #fails on version A and B

    def test_2(self):
        result = analyze_sentiment("The design is beautiful, but the app crashes too much.")
        self.assertEqual(result, "negative")

    def test_3(self):
        result = analyze_sentiment("I don’t hate it.")
        self.assertEqual(result, "positive") #fails on version A and B

    def test_4(self):
        result = analyze_sentiment("I used the app yesterday.")
        self.assertEqual(result, "neutral")  # will fail because model isn't trained on neutral

    def test_5(self):
        result = analyze_sentiment("Terrible.")
        self.assertEqual(result, "negative")

    def test_6(self):
        result = analyze_sentiment("Amazing experience!")
        self.assertEqual(result, "positive")

    def test_7(self):
        result = analyze_sentiment("Gr8 job guys, luv this app!")
        self.assertEqual(result, "positive")

    def test_8(self):
        result = analyze_sentiment("Ths thing sux")
        self.assertEqual(result, "negative")
    def test_9(self):
        result = analyze_sentiment("Customer acquisition cost is too high for this to scale.")
        self.assertEqual(result, "negative")
    def test_10(self):
        result = analyze_sentiment("The campaign ROI exceeded expectations.")
        self.assertEqual(result, "positive")
    def test_11(self):
        result = analyze_sentiment("Yeah, this app is so fast — it only froze five times today.")
        self.assertEqual(result, "negative")
    def test_12(self):
        result = analyze_sentiment("The customer service was slow, but the representative was kind.")
        self.assertEqual(result, "neutral") # will fail because model isn't trained on neutral
    def test_13(self):
        result = analyze_sentiment("It’s not bad at all.")
        self.assertEqual(result, "positive")
    def test_14(self):
        result = analyze_sentiment("I wouldn’t say it’s great.")
        self.assertEqual(result, "neutral") # will fail because model isn't trained on neutral
    def test_15(self):
        result = analyze_sentiment("meh")
        self.assertEqual(result, "negative")
    def test_16(self):
        result = analyze_sentiment("The user clicked the button three times.")
        self.assertEqual(result, "neutral") # will fail because model isn't trained on neutral
    def test_17(self):
        result = analyze_sentiment("The onboarding was clear, the UI was polished, and overall the app functioned well — though it could use a few speed improvements.")
        self.assertEqual(result, "positive")
    def test_18(self):
        result = analyze_sentiment("This update is a huge improvement")
        self.assertEqual(result, "positive")
    def test_19(self):
        result = analyze_sentiment("Could be worse, I guess.")
        self.assertEqual(result, "neutral") # will fail because model isn't trained on neutral
    def test_20(self):
        result = analyze_sentiment("Worst. App. Ever.")
        self.assertEqual(result, "negative")

if __name__ == "__main__":
    unittest.main()