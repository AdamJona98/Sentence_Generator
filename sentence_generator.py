import random

class SentenceGenerator:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    def load_words(self, file_path):
        try:
            with open(file_path, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Szöveges fájl nem található. Ellenőrizd az útvonalat!")
            return []

    def generate_sentence(self, num_words):
        if not self.words:
            return "A szöveges fájl nem tartalmaz szavakat."
        
        if num_words > len(self.words):
            num_words = len(self.words)
        
        sentence = " ".join(random.sample(self.words, k=num_words))
        return sentence.capitalize() + "."
