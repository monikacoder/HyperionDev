import spacy

################  Task 1.1 ######################
''' Code extract 1. Finding similarity between cat, monkey and banana.
'''
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"The similarity between {word1} and {word2} is : {word1.similarity(word2)}")
print(f"The similarity between {word3} and {word2} is : {word3.similarity(word2)}")
print(f"The similarity between {word3} and {word1} is : {word3.similarity(word1)}")

'''
Important findings from the program above.
1. The similarity between cat and monkey is 0.59, which means, Spacy was able to identify that both words have something common, i.e. they are animals.
2. The similarity between 'monkey and banana' was 0.40 which is lesser than between 'monkey and cat'. 
        However the rating of 0.40 means the Spacy was able to find something common between monkey and banana, i.e., monkey eat banana.
3. The similarity between cat and banana was least , 0.22, which means there wasn't something common between them.
'''

################  Task 1.2 ######################
''' New example. Finding similarity between paris, london, france.
'''
nlp = spacy.load('en_core_web_md')
word1 = nlp("paris")
word2 = nlp("london")
word3 = nlp("france")
print(f"The similarity between {word1} and {word2} is : {word1.similarity(word2)}")
print(f"The similarity between {word3} and {word2} is : {word3.similarity(word2)}")
print(f"The similarity between {word3} and {word1} is : {word3.similarity(word1)}")

'''
Interesting findings from the above program.
The similarity between france and london is 0.44 which is more than the similarity between france and paris which is 0.23. 
These results are bit strange as the paris is capital of france, so their similarity should have been greater. 
'''


################  Task 1.3 ######################
''' Code extract 2. Working with vectors
'''
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


################  Task 1.4 ######################
''' Code extract 3. Working with sentences.
'''
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
                "Hello, there is my car",
                "I\'ve lost my car in my car",
                "I\'d like my boat back",
                "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)