from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from split_text import split_text_class


class bleu_score_class():
    _p = split_text_class(
    )  # this is an object for spliting all texts that we need it to split

    def __init__(self, hypothese='', *references):
        ''' each bleu_score_class object has hypothese and references '''
        self.references = references
        self.hypothese = hypothese

    def calculate_bleu_score(self):
        ''' this is the main method to calculate the bleu score '''
        nb_references = len(self.references)
        # calculate the number of reference
        if nb_references > 0:
            lenght = len(bleu_score_class._p.spliting_text(self.references[0]))
            # calculate the number of sentences
            if lenght == 1:
                ''' 1 or more references with 1 sentence: '''
                ref = []
                for reference in self.references:
                    # split each one of the references
                    splited_reference = bleu_score_class._p.spliting_sentence(
                        reference)
                    ref.append(splited_reference)
                hypo = bleu_score_class._p.spliting_sentence(self.hypothese)
                # split the hypothese
                bleu_score = sentence_bleu(ref, hypo)
                # calculate the sentence-level bleu score
                return bleu_score
            elif lenght > 1:
                ''' 1 or more references with more than 1 sentence: '''
                ref = []
                for reference in self.references:
                    # split each one of the references
                    splited_reference = bleu_score_class._p.spliting_text(
                        reference)
                    ref.append(splited_reference)
                ordered_references = zip(*ref)
                ordered_references = list(map(list, ordered_references))
                # here we sort the sentences in way that each sentence
                # of hypothese have 1 or more reference sentences
                hypo = bleu_score_class._p.spliting_text(self.hypothese)
                # split the hypothese
                bleu_score = corpus_bleu(ordered_references, hypo)
                # calculate the corpus-level bleu score
                return bleu_score
            else:
                # references = ''
                return 0
        else:
            # references = []
            return 0


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# b = bleu_score_class('my name', 'my name is hamza')
# print(b.calculate_bleu_score())
# ------> I have to add Smoothing, multibleu and auto reweigh techniques
# ----------------------------------2----------------------------------
# b = bleu_score_class('my name is hamza jamil.', 'my name is hamza jamal,',
#                      'my name is hamza jamalo.')
# print(b.calculate_bleu_score())
# ------> It works good
# ----------------------------------3----------------------------------
#
