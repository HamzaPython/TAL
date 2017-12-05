from nltk.tokenize import regexp_tokenize, wordpunct_tokenize


class split_text():
    def __init__(self, text):
        self.text = text

    def spliting_sentence(self):
        ''' this method is used to split just 1 sentense'''
        return wordpunct_tokenize(self.text)

    def spliring_text(self):
        ''' this method is used to split more than 1 sentense (text)'''
        pattern = r'[^\n\t\;\:\?\!\,\.]+'
        sentenses = regexp_tokenize(
            self.text, pattern)  # here we split the text to multiple sentenses
        words = list(
            map(lambda sentense: wordpunct_tokenize(sentense), sentenses))
        # here we split each sentence to multiple words
        return words

    def __str__():
