class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        return [candidate for candidate in possible_anagrams 
                if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word]