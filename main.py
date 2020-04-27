from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivy.uix.screenmanager import *


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('SignUp.kv')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        return self.screen

if __name__ == '__main__':
	Test().run()
 