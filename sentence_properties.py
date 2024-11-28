class SentenceProperties:
    def __init__(self):
        self.font_styles = ["Helvetica", "Courier", "Comic Sans MS", "Impact"]
        self.font_size = 16
        self.font_color = "black"
        self.sentence_length = 5
        self.font_style_index = 0

    def get_font_style(self):
        return self.font_styles[self.font_style_index]

    def set_font_style_index(self, index):
        if 0 <= index < len(self.font_styles):
            self.font_style_index = index

    def get_font_size(self):
        return self.font_size

    def set_font_size(self, size):
        self.font_size = size

    def get_font_color(self):
        return self.font_color

    def set_font_color(self, color):
        self.font_color = color

    def get_sentence_length(self):
        return self.sentence_length

    def set_sentence_length(self, length):
        self.sentence_length = length
