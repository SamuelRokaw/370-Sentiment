The first option for training is more accurate because it has a larger sample size but is limited only to positive and negative outcomes
The second option has less samples but can do negative, neutral, and positive.
The problem with the second option is the input "This product is bad" is analyzed as a neutral review which isn't right.
That is why by default the program is trained off the first option.
You can change the programs training by uncommenting/commenting out the correct lines in the section of Sentimentanal.py in the CSV Reading section