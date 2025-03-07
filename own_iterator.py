class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.value = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):

        len_of_sen = len(self.words)

        if self.value >= len_of_sen:
            raise StopIteration

        current = self.value
        self.value += 1
        return self.words[current]


my_sentence = Sentence("I am an iterator. Can you see me iterating?")

for word in my_sentence:
    print(word)
