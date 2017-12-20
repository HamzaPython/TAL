import sys
import numpy
from split_text import split_text_class


class wer_score_class:
    def __init__(self, h, *r):
        self._p = split_text_class(h, r)
        self.r = []
        for reference in r:
            self.r.append(self._p.spliting_sentence(reference))
        self.h = self._p.spliting_sentence(h)

    def distance(self, r, h):
        d = numpy.zeros((len(r) + 1) * (len(h) + 1))
        d = d.reshape((len(r) + 1, len(h) + 1))
        for i in range(len(r) + 1):
            for j in range(len(h) + 1):
                if i == 0:
                    d[0][j] = j
                elif j == 0:
                    d[i][0] = i
        for i in range(1, len(r) + 1):
            for j in range(1, len(h) + 1):
                if r[i - 1] == h[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    substitute = d[i - 1][j - 1] + 1
                    insert = d[i][j - 1] + 1
                    delete = d[i - 1][j] + 1
                    d[i][j] = min(substitute, insert, delete)
        return d

    def calculate_wer_score(self):
        wer_scores = []
        for reference in self.r:
            d = self.distance(reference, self.h)
            wer_score = d[len(reference)][len(self.h)]  #/ len(reference)
            # we calculate wer(each_reference, hypothese) score
            wer_scores.append(wer_score)
        result = max(wer_scores)
        # we calculate wer(closest_reference, hypothese) score
        return result


# -------------------------------Exemples:-----------------------------
# ----------------------------------1----------------------------------
# valeur1 = "who are you?"
# valeur2 = "who are you?"
# w = wer_score_class(valeur1, valeur2)
# print(w.calculate_wer_score())
# ------> It works good
