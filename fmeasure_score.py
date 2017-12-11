from nltk.metrics.scores import f_measure
from split_text import split_text_class


class fmeasure_score_class():
    def __init__(self, hypothese='', *references):
        ''' each bleu_score_class object has hypothese and references '''
        self.references = references
        self.hypothese = hypothese
        self._p = split_text_class(hypothese, references)
        # _p is a private attribut for spliting
        # all texts that we need it to split

    def sentence_fmeasure(self, references, hypothese):
        fmeasure_scores = []
        hypothese_set = set(hypothese)
        for reference in references:
            reference_set = set(reference)
            fmeasure_score = f_measure(reference_set, hypothese_set)
            # we calculate f_measure(set(each_reference), set(hypothese)) score
            fmeasure_scores.append(fmeasure_score)
        fmeasure_final_score = max(fmeasure_scores)
        # we calculate f_measure(set(closest_reference), set(hypothese)) score
        return fmeasure_final_score

    def corpus_fmeasure(self, references, hypothese):
        fmeasure_score_sentences = []
        for hypo, ref in zip(hypothese, references):
            fmeasure_score_sentence = self.sentence_fmeasure(ref, hypo)
            fmeasure_score_sentences.append(fmeasure_score_sentence)
        fmeasure_final_score = sum(fmeasure_score_sentences) / len(
            fmeasure_score_sentences)
        return fmeasure_final_score

    def calculate_fmesure_score(self):
        ''' this is the main method to calculate the F-measure score '''
        hypo, ref, has_one_sentence = self._p.split_references_hypothesis()
        if ref is None:
            return 0
        elif has_one_sentence:
            ''' 1 or more references with 1 sentence: '''
            fmeasure_score = self.sentence_fmeasure(ref, hypo)
            # calculate the sentence-level fmeasure score
            return fmeasure_score
        else:
            ''' 1 or more references with more than 1 sentence: '''
            fmeasure_score = self.corpus_fmeasure(ref, hypo)
            # calculate the corpus-level fmeasure score
            return fmeasure_score


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# f = fmeasure_score_class('my name', 'my name is hamza')
# print(f.calculate_fmesure_score())
# ------> It works good
# ----------------------------------2----------------------------------
# f = fmeasure_score_class(
#     'my name is hamza jamal, I m 22 years old, you?',
#     'name my hamza jamali is, I m 22 years old, and you?',
#     'my name is hamza jamalo. I m 22 years old, what about you?')
# print(f.calculate_fmesure_score())
# ------> It works good
# ----------------------------------3----------------------------------
#
