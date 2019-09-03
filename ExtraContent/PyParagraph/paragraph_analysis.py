import re
import os

approximate_words = 0
approximate_sentences = 0
total_letter_count = 0
average_sentence_length = 0

def user_choice():
    user_decision = input("Which text would you like anaylsis on (1 or 2)? ")
    if user_decision == '1':
        return 'paragraph_1.txt'
    else:
        return 'paragraph_2.txt'

pick_paragraph = user_choice()

text_path = os.path.join('raw_data', pick_paragraph)

with open(text_path, 'r') as f:
    for line in f:
        for word in line.split():
            if '.' in word:
                approximate_sentences += 1
            total_letter_count += len(word)
            approximate_words +=1

print('Approx sentences :', approximate_sentences)
print('Approx words :', approximate_words)
print('Averate letter count :', round(total_letter_count/approximate_words,2))
print('Average Sentence Length :', round(approximate_words/approximate_sentences,2))
