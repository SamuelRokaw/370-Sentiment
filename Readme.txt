# Sentiment Analysis Assignment for CPSC 370: "AI in Business"
https://three70-sentiment.onrender.com/
This repository contains a sentiment analysis program developed as part of the CPSC 370 course. The program uses machine learning to classify text input as either positive or negative based on a trained model.

## Data Sets
1. **Primary Training Data**: 
   - A dataset of 1.6 million reviews labeled as positive or negative.
   - This large dataset was chosen to improve the model's training and accuracy.

2. **Secondary Data**:
   - A smaller dataset of 439 reviews labeled as positive, neutral, or negative.
   - This dataset was not used for training due to its smaller size 

## Functionality
The program analyzes input text and predicts whether the sentiment is positive or negative. While the model performs well in most cases, certain sentence structures or linguistic nuances may lead to unexpected results.

### Known Limitations
- **Double Negatives**: 
  - Example: "not not good" is classified as negative. The expected result is positive, but the model fails to account for the cancellation of the double negatives.
- **Ambiguous Sentence Structures**:
  - Example: "if you are thinking of buying this, don't buy it" is correctly classified as negative.
  - However, "if you are thinking of buying this, don't" is incorrectly classified as positive due to the sentence's structure.

## Example Usage
- Input: "This product is amazing!"
  - Output: Positive
- Input: "I wouldn't recommend this to anyone."
  - Output: Negative

## Future Improvements
- Enhance the model to better handle double negatives and complex sentence structures.
- Incorporate the smaller dataset for additional testing and validation.
- Explore advanced natural language processing techniques to improve accuracy.

## Notes
This project demonstrates the challenges of sentiment analysis, particularly when dealing with nuanced language. It highlights the importance of dataset quality, model training, and handling edge cases in natural language processing.

