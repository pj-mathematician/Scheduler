#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from datetime import time
from datetime import date
from kivy.properties import ObjectProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDTimePicker
import os
import MainApp

kv1 = 'loginwindow.kv'
kv2 = 'newinput.kv'
kv3 = 'signupwindow.kv'

class loginwindow(Screen):
    pass


class signupwindow(Screen):
    pass


class newinput(Screen):
    pass
	
class Test(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Purple"
        Builder.load_file(kv1)
        Builder.load_file(kv2)
        Builder.load_file(kv3)
        self.sm = ScreenManager()
        self.sm.add_widget(loginwindow())
        self.sm.add_widget(signupwindow())
        self.sm.add_widget(newinput())
        return self.sm

    dialog = None
    previous_time = ObjectProperty()
    dynamic_ip=None
    fixedtimedict={}

    def time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.show)
        self.time_dialog.open()
    def show(self,instance,time):
    	self.sm.get_screen('ninput').ids[self.dynamic_ip].text = str(time)
    	self.fixedtimedict[self.dynamic_ip]=time
    
    def MainApp(self):
    	#os.system('MainApp.py')
    	self.stop()
    	MainApp.TestNavigationDrawer().run()
    
    def on_signup(self, *args):
        self.dialog.dismiss()
        self.sm.current = 'ninput'

    def show_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(title='Confirmation',
                                   text='You have been registered.',
                                   size_hint=(0.4, 0.3),
                                   buttons=[
                                   MDFlatButton(text='CANCEL',on_release=self.dialog_close),
                                   MDFlatButton(text="OK!", on_release=self.on_signup)
                                   ])

        self.dialog.open()
       
    def dialog_close(self, *args):
        self.dialog.dismiss()
    def on_stop(self):
    	return True
if __name__ == '__main__':
    Test().run()