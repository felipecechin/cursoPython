import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print("funcSelf")

Button.funcSelf = funcSelf

class MinhaTela(BoxLayout):
    def funcRoot(self):
        print("funcRoot")


class Estudo1App(App):
    def funcApp(self):
        print("funcApp")

janela = Estudo1App();
janela.run()