import kivy
kivy.require("1.9.1")
from kivy.app import App

code = """
BoxLayout:
    Button:
        text: "1"
    Button: 
        text: "2"
"""

from kivy.lang import Builder

class Estudo1App(App):
    def build(self):
        return Builder.load_string(code)

janela = Estudo1App();
janela.run()