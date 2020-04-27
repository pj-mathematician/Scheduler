from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp



class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('login.kv')

    def build(self):
        self.theme_cls.theme_style = "Dark"  

        screen = Screen()
    	


        return self.screen



Test().run()