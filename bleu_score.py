from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from split_text import split_text_class


class bleu_score_class():
    def __init__(self, hypothese='', *references):
        ''' each bleu_score_class object has hypothese and references '''
        self.references = references
        self.hypothese = hypothese
        self._p = split_text_class(hypothese, references)
        # _p is a private attribut for spliting
        # all texts that we need it to split

    def calculate_bleu_score(self):
        ''' this is the main method to calculate the bleu score '''
        hypo, ref, has_one_sentence = self._p.split_references_hypothesis()
        if ref is None:
            return 0
        elif has_one_sentence:
            ''' 1 or more references with 1 sentence: '''
            bleu_score = sentence_bleu(ref, hypo)
            # calculate the sentence-level bleu score
            return bleu_score
        else:
            ''' 1 or more references with more than 1 sentence: '''
            bleu_score = corpus_bleu(ref, hypo)
            # calculate the corpus-level bleu score
            return bleu_score


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# b = bleu_score_class('my name', 'my name is hamza')
# print(b.calculate_bleu_score())
# ------> I have to add Smoothing, multibleu and auto reweigh techniques
# ----------------------------------2----------------------------------
# b = bleu_score_class('my name is hamza jamal,', 'my name is hamza jamali,',
#                      'my name is hamza jamalo.')
# print(b.calculate_bleu_score())
# ------> It works good
# ----------------------------------3----------------------------------
#
