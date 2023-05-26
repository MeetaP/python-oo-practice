"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    Initialize constructor that takes file as argument and 
    returns number of word read as output
    """
    def __init__(self, word_file):
        # Define empty list to store read words from file
        self.word_list = []
        with open(word_file) as word_file:
            for word in word_file:
                #Append each word to list
                self.word_list.append(word.strip())   
        print('{} words read'.format(len(self.word_list)))

    def random(self):
        """Call random method from package imported 
        to generate a random word from the list
        """
        return random.choice(self.word_list)
#Create subclass RandomWordFinder
class RandomWordFinder(WordFinder):
    """ Call constructor that skips blank lines and commented words from list
    """
    def __init__(self, word_file):
        self.skip_word_list = []
        with open(word_file) as word_file:
            for word in word_file:
                if not word or word.startswith('#'):
                    continue
                self.skip_word_list.append(word.strip())

    def random(self):
        return random.choice(self.skip_word_list)

#Create object of parent class
wf = WordFinder("/Users/meetapandit/DE_Bootcamp/python-oo-practice/words.txt")

#Create object of subclass
rwf = RandomWordFinder("/Users/meetapandit/DE_Bootcamp/python-oo-practice/words.txt")
#Call random method from parent class
print(wf.random())
print(wf.random())
print(wf.random())
#Call random method from subclass
print(rwf.random())
