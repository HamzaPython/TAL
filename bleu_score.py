from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from split_text import split_text_class


class bleu_score():
    p = split_text_class()

    def __init__(self, hypothese='', *references=['']):
        self.references = references
        self.hypothese = hypothese

    def calculate_bleu_score(self):
        if len(self.references) > 1:
            pass
        elif len(self.references) == 1:
            p.spliting_text(self.references)
