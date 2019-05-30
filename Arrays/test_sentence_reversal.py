"""
Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
"""

class Reversal():

    def __init__(self, sentence):
        self.clear_sent = " ".join(sentence.split())
        
    def rev_sentence(self, clear_sent):
        """
        Reverses 
        """
        reversed_sent = ""
        for i in range(len(self.clear_sent)-1, -1, -1):
            print("Index: ", i)
            reversed_sent += self.clear_sent[i]
        return reversed_sent



sentence = "          My name        is     Maria        "
reversal = Reversal(sentence)
reversal.rev_sentence(sentence)


# """
# Solution
# Fill out your solution below:
# """

# def rev_word(s):
#     return " ".join(reversed(s.split()))
