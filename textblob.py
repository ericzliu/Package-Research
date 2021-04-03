import random
from textblob.blob import TextBlob, Word    ## imported TextBlob object
                                            ## Textblob library also has an in-build object known as Word
                                                ## allows one to create a word object and apply a function directly to it


## Defined string "blob" that contains the text we are going to use
blob = TextBlob("TextBlob is a Python (2 and 3) library for processing textual data. \
It provides a simple API for diving into common natural language processing (NLP) tasks \
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.")


## Sample code found online and revised
## Parts of speech tagging
nouns = list()
for word, tag in blob.tags:
    if tag == 'NN':                             ## Uses parts of speech tagging - each word has its own tag... if the tag of 
        nouns.append(word.lemmatize())              ## a word in blob is identified to be == noun,
                                                    ## append method adds item to end of list; then lemmatizes appended item/word
                                                ## Lemmatization reduces the word to its root form

print ("This text is talking about:")
for item in random.sample(nouns, 3):            ## Extracts the list of nouns in list, picking 3 of them; value can be adjusted accordingly
    word = Word(item)
    print (word.pluralize)                      ## Prints extracted items once pluralized


## Revised version of sample code, this time with textBlob looking for proper nouns 
## The information provided now specifies main ideas within the text such as Python, NLP, etc.
def properNouns():
    """Parts of speech tagging; appends items/words in blob and lemmatizes appended items"""
    properNouns = list()
    for word, tag in blob.tags:
        if tag == 'NNP':                            ## Parts of speech tagging - if tag == proper noun, then
            properNouns.append(word.lemmatize())        ## append method adds item to end of list, then lemmatizes appended item/word

    print ("This text talks about:")
    for item in random.sample(properNouns, 3):      ## Extracts the list of properNouns in list, picking 3 of them; value can be adjusted accordingly
        word = Word(item)                           
        print (word)                                ## Prints the extracted items

properNouns()


def translate():
    """Detect the blob string language and print in translated form
    
    Args:
        No arg function; takes no parameters, simply prints translated string
    
    Returns:
        No explicit returns. Prints translated blob from English to Hindi
    """
    blob.detect_language()                              ## detects the language in the blob "string" (technically not necessary here)
    print("Here is the text translated into Hindi:")    
    print (blob.translate(from_lang="en", to = "hi"))   ## translates blob from English to Hindi

translate()

