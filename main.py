from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
kvf='Login.kv'

class loginwindow(Screen):
	pass
class signupwindow(Screen):
	pass	




class Test(MDApp):
   def build(self):
   	self.theme_cls.theme_style = "Dark"  
   	Builder.load_file(kvf)
   	self.sm = ScreenManager()
   	self.sm.add_widget(loginwindow())
   	self.sm.add_widget(signupwindow())
   	return self.sm
		

if __name__ == '__main__':
	Test().run()