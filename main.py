from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
kv='Login.kv'

class loginwindow(Screen):
	pass
class signupwindow(Screen):
	pass	

sm=ScreenManager()
sm.add_widget(loginwindow(name='login'))
sm.add_widget(signupwindow(name='signup'))
sm.current='login'
class Test(MDApp):



    def build(self):
  
    	self.theme_cls.theme_style = "Dark"  
    	screen = Screen()
    	self.root = Builder.load_file(kv)



Test().run()