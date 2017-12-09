from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from split_text import split_text_class


class bleu_score_class():
    p = split_text_class()

    def __init__(self, hypothese='', *references):
        self.references = references
        self.hypothese = hypothese

    def calculate_bleu_score(self):
        nb_references = len(self.references)
        if nb_references >= 1:
            lenght = len(bleu_score_class.p.spliting_text(self.references[0]))

            if lenght == 1:
                ref = []
                for reference in self.references:
                    splited_reference = bleu_score_class.p.spliting_sentence(
                        reference)
                    ref.append(splited_reference)
                hypo = bleu_score_class.p.spliting_sentence(self.hypothese)
                print(ref)
                print(hypo)
                bleu_score = sentence_bleu(ref, hypo)
                return bleu_score
            elif lenght > 1:
                ref = []
                for reference in self.references:
                    splited_reference = bleu_score_class.p.spliting_text(
                        reference)
                    ref.append(splited_reference)
                ordered_references = zip(*ref)
                ordered_references = list(map(list, ordered_references))
                hypo = bleu_score_class.p.spliting_text(self.hypothese)
                print(ordered_references)
                print(hypo)
                bleu_score = corpus_bleu(ordered_references, hypo)
                return bleu_score


# b = bleu_score_class('my name is hamza jamil.', 'my name is hamza jamal,',
#                      'my name is hamza jamalo.')
# print(b.calculate_bleu_score())
