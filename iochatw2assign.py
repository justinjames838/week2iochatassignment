import nltk
import textblob
from textblob import Word,TextBlob
import random


tag_to_text ="""     CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there 
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective
    JJR adjective, comparative
    JJS adjective, superlative
    LS list marker 
    MD modal
    NN noun, singular
    NNS noun plural 
    NNP proper noun, singular
    NNPS proper noun, plural 
    PDT predeterminer
    POS possessive ending
    PRP personal pronoun
    PRP$ possessive pronoun
    RB adverb
    RBR adverb, comparative
    RBS adverb, superlative
    RP particle
    TO to
    UH interjection
    VB verb, base form
    VBD verb, past tense
    VBG verb, gerund/present participle
    VBN verb, past participle
    VBP verb, sing. present, non-3d
    VBZ verb, 3rd person sing. present
    WDT wh-determiner
    WP wh-pronoun
    WP$ possessive wh-pronoun
    WRB wh-abverb"""

tag_to_text_dict = {}
for line in tag_to_text.split("\n"):
	 line = line.strip()
	 tag_to_text_dict[line.split()[0]] = " ".join(line.split()[1:])


sentence = input("Enter your sentence : ")
parts_of_speech = nltk.pos_tag(nltk.word_tokenize(sentence))
print("\nThe parts of speech in your sentence are : \n")
for tup in parts_of_speech:
		
	if(tup[0]!='.' and tup[0]!=','):
	    print(tup[0] + " : " + tag_to_text_dict[tup[1]])


print("\nEnter a word you would like synonyms and antonyms for : ")
word = Word(input())

synonyms = list(set([l.name() for syn in word.get_synsets() for l in syn.lemmas()]))
antonyms = list(set([ant.name() for syn in word.get_synsets() for l in syn.lemmas() for ant in l.antonyms()]))

print(f" Synonyms : "+",".join(synonyms))
print(f" Antonyms : "+",".join(antonyms))

languages = [('ar','Arabic'),('zh-CN','Chinese'),('sk','Slovakian'),('ja','Japanese')]
lang = random.choice(languages)

sentence = TextBlob(input("\nEnter a sentence you'd like to see translated to another language : "))
print("\nYour sentence translated to " + lang[1] + " is : " + str(sentence.translate(to = lang[0])))

print("\nEnter a word you'd like definitions for : ")
word2 = Word(input())

print("\nDefinitions: ")

for definition in word2.definitions:
  print(definition)


