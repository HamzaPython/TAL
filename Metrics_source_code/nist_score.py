from nltk.translate.nist_score import sentence_nist, corpus_nist
from split_text import split_text_class


class nist_score_class():
    def __init__(self, hypothese='', *references):
        ''' each nist_score_class object has hypothese and references '''
        self.references = references
        self.hypothese = hypothese
        self._p = split_text_class(hypothese, references)
        # _p is a private attribut for spliting
        # all texts that we need it to split

    def calculate_nist_score(self):
        ''' this is the main method to calculate the nist score '''
        hypo, ref, has_one_sentence = self._p.split_references_hypothesis()
        if ref is None:
            return 0
        elif has_one_sentence:
            ''' 1 or more references with 1 sentence: '''
            nist_score = sentence_nist(ref, hypo)
            # calculate the sentence-level nist score
            return nist_score
        else:
            ''' 1 or more references with more than 1 sentence: '''
            nist_score = corpus_nist(ref, hypo)
            # calculate the corpus-level nist score
            return nist_score


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# n = nist_score_class('my friend is yassin, you?',
#                      'my friend is yassin, and you?',
#                      'my friend is yassin, how about you')
# print(n.calculate_nist_score())
#
# ------> It works good
# ----------------------------------2----------------------------------
# n = nist_score_class('my name is hamza jamal', 'my name is hamza jamal')
# print(n.calculate_nist_score())
# ------> It works good too
# ----------------------------------3----------------------------------
#
