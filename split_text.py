from nltk.tokenize import regexp_tokenize, wordpunct_tokenize


class split_text_class():
    def spliting_sentence(self, text=''):
        ''' this method is used to split just 1 sentense '''
        return wordpunct_tokenize(text)

    def spliting_text(self, text=''):
        ''' this method is used to split more than 1 sentense (text)'''
        pattern = r'[^\n\t\;\:\?\!\,\.]+'

        # here we will split the text to multiple sentenses:
        sentenses = regexp_tokenize(text, pattern)

        # here we will split each sentence to multiple words:
        words = list(
            map(lambda sentense: wordpunct_tokenize(sentense), sentenses))
        return words

    ''' this 2 methods (str and repr) are
    used in this code to increase readability '''

    def __str__(self):
        return "this is an object from split_text_class class"

    def __repr__(self):
        return "split_text_class({0.text})".format(self)
