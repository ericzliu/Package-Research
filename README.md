
# Package-Research
This project involves identifying and analyzing a Python package and presenting a summary and example code that demonstrates what the package can do.

## Package Summary - Textblob
In this package research project I utilized Textblob, a powerful text analysis package.
Textblob is essentially a Python library used to process textual data. It features many uses such as spelling correction, sentiment analysis, part-of-speech tagging, etc. by providing a simple API.
Textblob acts just like traditonal Python strings, allowing users to perform various methods on specific text.

## Installing Textblob
To install Textblob, run the following commands into your terminal:

- $ pip install -U textblob
- $ python -m textblob.download_corpora

Textblob works for both Python 2 and 3.

## Supported Features and Best-Practices

As mentioned before, Textblob features many common natural langauge processing (NLP) tasks:

+ Spelling correction
+ Sentiment analysis
+ Part-of-speech tagging
+ Pluralization/Singularization
+ Lemmatization
+ Translation
+ Noun phrase extraction
+ Tokenization
+ Word and phrase frequencies

## Textblob [Quickstart Tutorial](https://textblob.readthedocs.io/en/dev/quickstart.html)
![quickstart](https://user-images.githubusercontent.com/81776233/113464204-f0705c00-93f8-11eb-9436-b0d4ba804538.PNG)

## Brief explanation of Code
In textblob.py, we have imported TextBlob object. Textblob library also has an in-build object known as Word, which allows one to create a word object and apply a function directly to it, so Wod is also imported. Random is imported which allows us to take a random value from the list sample appended within the code.

The code creates a Textblob string named "blob" which we use to store our text (line 8). Then, we utilize speech tagging in order to find all words within the blob string that have the NN tag, or noun tag (lines 15-18). Once this is done, the item/word is added to a list and the item is lemmatized. A random sample of these words is chosen from the appended list from the blob string, and the items is pluralized and printed as a result (lines 22-25).
This is all done for proper nouns as well (lines 30-42).

Lastly, the blob text is translated from English into Hindi (lines 45-58).

## Future idea
In this midterm package research project, I showed a very basic implementation of Textblob. Doing research on packages has made me interested in the kinds of things they can accomplish, and it certainly made me much more aware of Textblob's other uses. One popular use (that I played around with but did not use for this project) was the sentiment analysis that Textblob has to offer. If Textblob were to be combined Tweepy, it would be very interesting to do some kind of Twitter Sentiment Analysis with a Raspberry Pi (like the example you provided us in the midterm project). Raspberry Pi is something I played around with this past winter break, and I was aware of its Python capabilities before taking this course. It is certainly very possible for me to create something that connects my knowledge of these packages with some hardware to create a simplistic project for sentiment analysis.

