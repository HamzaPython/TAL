from nltk.tokenize import regexp_tokenize, wordpunct_tokenize


class split_text_class():
    def __init__(self, hypothese='', *references):
        ''' each metrics has an hypothese and references '''
        self.references = references[0]
        self.hypothese = hypothese

    def spliting_sentence(self, text=''):
        ''' this method is used to split just 1 sentense '''
        return wordpunct_tokenize(text)

    def spliting_text(self, text=''):
        ''' this method is used to split more than 1 sentense (text)'''
        punctuations = ';:?!,.'
        spaces = r'\n\t'
        pattern = r'[^{}+{}]+'.format(punctuations, spaces)
        # here we will split the text to multiple sentenses:
        sentenses = regexp_tokenize(text, pattern)

        # here we will split each sentence to multiple words:
        words = list(
            map(lambda sentense: wordpunct_tokenize(sentense), sentenses))
        return words

    def split_references_hypothesis(self):
        ''' this is the main method that gives the metrics their parameters'''
        nb_references = len(self.references)
        # calculate the number of reference
        if nb_references > 0:
            lenght = len(self.spliting_text(self.references[0]))
            # calculate the number of sentences
            if lenght == 1:
                ''' 1 or more references with 1 sentence: '''
                ref = []
                for reference in self.references:
                    # split each one of the references
                    splited_reference = self.spliting_sentence(reference)
                    ref.append(splited_reference)
                hypo = self.spliting_sentence(self.hypothese)
                # split the hypothese
                return hypo, ref, isinstance(hypo[0], str)
            elif lenght > 1:
                ''' 1 or more references with more than 1 sentence: '''
                ref = []
                for reference in self.references:
                    # split each one of the references
                    splited_reference = self.spliting_text(reference)
                    ref.append(splited_reference)
                ordered_references = zip(*ref)
                ordered_references = list(map(list, ordered_references))
                # here we sort the sentences in way that each sentence
                # of hypothese have 1 or more reference sentences
                hypo = self.spliting_text(self.hypothese)
                # split the hypothese
                return hypo, ordered_references, isinstance(hypo[0], str)
            else:
                # references = ''
                return self.hypothese, None, False
        else:
            # references = []
            return self.hypothese, None, False

    ''' this 2 methods (str and repr) are
    used in this code to increase readability '''

    def __str__(self):
        return "this is an object from split_text_class class"

    def __repr__(self):
        return "split_text_class({0.text})".format(self)


# p = split_text_class('my name is hamza jamil. I m 22 years old', 'my name is hamza jamilo. my age is 22 years old', 'my name is khalid. my age is 23 years old')
# hypo, ref, has_one_sentence = p.split_references_hypothesis()
# print(hypo)
# print(ref)
# print(has_one_sentence)
