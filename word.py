class Word(object):
    def __init__(self, w, meaning, synonyms, expression, example):
        self.text = w
        self.meaning = meaning
        self.synonyms = synonyms
        self.expression = expression
        self.example = example