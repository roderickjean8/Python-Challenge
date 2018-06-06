# import libraries
import os
	
# navigate to file
file = 'raw_data/paragraph_1.txt'
	
# declare variables
letter_count = 0
	
# open file
with open(file, 'r') as txtfile:
	paragraph = txtfile.read()
	
    # define word count
	word_count = paragraph.count(" ") + 1
	
    # define sentence count
	sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
	
    # calculate average letter count
	for character in paragraph:
	    if character.isalpha():
	        letter_count += 1 
	avg_letter_count = letter_count/word_count
	
    # define average sentence length
	avg_sentence = word_count/sentence_count
	
# print analysis results
print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count:", word_count)
print("Approximate Sentence Count:", sentence_count)
print("Approximate Letter Count:", avg_letter_count)
print("Average Sentence Length:", avg_sentence)