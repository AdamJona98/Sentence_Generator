from tkinter import Tk, Label, StringVar, Scale, colorchooser, Button
from sentence_generator import SentenceGenerator

def create_app_window(sentence_props):
    root = Tk()
    root.title("app")
    root.geometry("600x500")

    generator = SentenceGenerator("words.txt")

    current_sentence = StringVar(value="Használd a gombokat a mondatgyártáshoz.")

    sentence_label = Label(
        root,
        textvariable=current_sentence,
        font=(sentence_props.get_font_style(), sentence_props.get_font_size()),
        fg=sentence_props.get_font_color(),
    )
    sentence_label.pack(pady=20)

    def generate_sentence():
        current_sentence.set(generator.generate_sentence(sentence_props.get_sentence_length()))
        update_label()

    def change_color():
        color = colorchooser.askcolor(title="Válassz színt")[1]
        if color:
            sentence_props.set_font_color(color)
            update_label()

    def update_label():
        """Frissíti a címke megjelenítését az aktuális tulajdonságok alapján."""
        sentence_label.config(
            font=(sentence_props.get_font_style(), sentence_props.get_font_size()),
            fg=sentence_props.get_font_color(),
        )

    Label(root, text="Mondathossz:").pack(pady=5)
    length_slider = Scale(
        root,
        from_=2,
        to=8,
        orient="horizontal",
        command=lambda val: [sentence_props.set_sentence_length(int(val)), update_label()],
    )
    length_slider.set(sentence_props.get_sentence_length())
    length_slider.pack()

    Label(root, text="Betűméret:").pack(pady=5)
    font_size_slider = Scale(
        root,
        from_=16,
        to=32,
        orient="horizontal",
        command=lambda val: [sentence_props.set_font_size(int(val)), update_label()],
    )
    font_size_slider.set(sentence_props.get_font_size())
    font_size_slider.pack()

    Label(root, text="Betűtípus:").pack(pady=5)
    font_style_slider = Scale(
        root,
        from_=0,
        to=len(sentence_props.font_styles) - 1,
        orient="horizontal",
        command=lambda val: [sentence_props.set_font_style_index(int(val)), update_label()],
    )
    font_style_slider.set(sentence_props.font_style_index)
    font_style_slider.pack()

    Label(root, text="Betűszín:").pack(pady=5)
    color_button = Button(root, text="Szín kiválasztása", command=change_color)
    color_button.pack()

    generate_button = Button(root, text="Mondat generálása", command=generate_sentence)
    generate_button.pack(pady=20)

    root.mainloop()
