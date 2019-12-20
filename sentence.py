class Sentence(str):
    def __init__(self):
        self.data = ""

    def __add__(self, phrase):
        self.data += self.__sentence_maker(phrase)
        return self

    def __sentence_maker(self, phrase):
        if not phrase:
            return ""
        phrase = phrase.capitalize()
        interrogatives = ("Who", "How", "When", "Is", "Are", "Whose", "Why")
        if phrase.startswith(interrogatives):
            return f"{phrase}? "
        else:
            return f"{phrase}. "

    @property
    def sentence(self):
        return self.data

    @sentence.setter
    def sentence(self, data):
        for d in data.split("."):
            self.data += self.__sentence_maker(d.strip())

    def __str__(self):
        return self.data


writing = Sentence()

while True:
    phrase = input("Say something: ")
    if phrase == "\end":
        break
    writing += phrase

print(writing.sentence)

writing.sentence = "how are you.       when are you coming.       who is this.      "

print(writing.sentence)
