from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):

    def build(self):
        box = BoxLayout(orientation="vertical")
        button = Button(text="Botão 1", font_size=30, on_release=self.incrementar)
        self.label = Label(text="Texto 1", font_size=30)
        box.add_widget(button)
        box.add_widget(self.label)

        self.x = 0

        return box

    def incrementar(self, button):
        self.x += 1
        self.label.text = str(self.x)


Teste().run()