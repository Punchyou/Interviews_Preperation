"""
Sentence Reversal
Problem
Given a string of words, reverse all the words.
For example:

Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove
all leading and trailing whitespace.
So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
"""
#Reverces all characters from sentence.
class Reversal():

    def __init__(self, sentence):
        self.clear_sent = " ".join(sentence.split())
        
    def rev_sentence(self):
        """
        Reverses every character in a sentence.
        """
        reversed_sent = ""
        for i in range(len(self.clear_sent)-1, -1, -1):
            reversed_sent += self.clear_sent[i]
        return reversed_sent

sentence = "          My name        is     Maria        "
reversal = Reversal(sentence)
reversal.rev_sentence()


# Reverses the order of the words.
class Reversal2():

    def __init__(self, sentence):
        self.clear_sent = " ".join(sentence.split()).split()
    
    def rev_words(self):
        """
        Reverses the order of the words in a sentence.
        """
        reversed_sent = ""
        for i in range(len(self.clear_sent)-1, -1, -1):
            reversed_sent += self.clear_sent[i] + " "
        return reversed_sent.rstrip()

sentence = "          My name        is     Maria        "
reversal = Reversal2(sentence)
reversal.rev_words()



# """
# Solution
# Fill out your solution below:
# """

# def rev_word(s):
#     return " ".join(reversed(s.split()))



# """
# Second Solution
# """

# def rev_word(s):

#     words = []
#     length = len(s)
#     spaces = [' ']

#     i = 0
#     while i < length:
#         if s[i] not in spaces:
#             word_start = i
#             while i < length and s[i] not in spaces:
#                 i += 1
#             words.append(s[word_start:i])
#         i += 1
#     return " ".join(reversed(words))
