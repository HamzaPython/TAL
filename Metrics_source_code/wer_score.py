import numpy
from split_text import split_text_class


class wer_score_class:
    def __init__(self, hypothesis, *references):
        self._p = split_text_class(hypothesis, references)
        self.references = []
        for reference in references:
            self.references.append(self._p.spliting_sentence(reference))
        self.hypothesis = self._p.spliting_sentence(hypothesis)

    def distance(self, reference):
        d = numpy.zeros((len(reference) + 1) * (len(self.hypothesis) + 1))
        d = d.reshape((len(reference) + 1, len(self.hypothesis) + 1))
        for i in range(len(reference) + 1):
            for j in range(len(self.hypothesis) + 1):
                if i == 0:
                    d[0][j] = j
                elif j == 0:
                    d[i][0] = i
        for i in range(1, len(reference) + 1):
            for j in range(1, len(self.hypothesis) + 1):
                if reference[i - 1] == self.hypothesis[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    substitute = d[i - 1][j - 1] + 1
                    insert = d[i][j - 1] + 1
                    delete = d[i - 1][j] + 1
                    d[i][j] = min(substitute, insert, delete)
        return d

    def calculate_wer_score(self):
        wer_scores = []
        for reference in self.references:
            d = self.distance(reference)
            wer_score = d[len(reference)][len(
                self.hypothesis)]  #/ len(reference)
            # we calculate wer(each_reference, hypothesis) score
            wer_scores.append(wer_score)
        result = max(wer_scores)
        # we calculate wer(closest_reference, hypothesis) score
        return result


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# valeur1 = "who are you?"
# valeur2 = "who are you?"
# w = wer_score_class(valeur1, valeur2)
# print(w.calculate_wer_score())
# ------> It works good
