from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class incrementador(BoxLayout):
    pass

class Teste(App):

    def build(self):
        self.x=0
        return incrementador()

    def incrementar(self, *args):
        self.x += 1
        return self.x

Teste().run()