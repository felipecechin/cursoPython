#coding = utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="Componente TextInput")

app = App()
app.build = build
app.run()