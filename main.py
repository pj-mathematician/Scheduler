#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from datetime import time
from datetime import date
from kivy.properties import ObjectProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDTimePicker
import MainApp
import mysqllog

kv1 = 'KivyFiles\\loginwindow.kv'
kv2 = 'KivyFiles\\newinput.kv'
kv3 = 'KivyFiles\\signupwindow.kv'

class loginwindow(Screen):
    pass


class signupwindow(Screen):
    pass


class newinput(Screen):
    pass
	
class Test(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
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
    inpasdialog=None
    inusedialog=None
    dynamic_ip=None
    val012=None
    previous_time = ObjectProperty()
    fixedtimedict={}

    def get_info(self):
        name = self.sm.get_screen('signup').ids.name.text
        email = self.sm.get_screen('signup').ids.email.text
        confirm_email = self.sm.get_screen('signup').ids.confirm_email.text
        password = self.sm.get_screen('signup').ids.password.text
        confirm_pass = self.sm.get_screen('signup').ids.confirm_pass.text

        print(name, email, confirm_email, password, confirm_pass)



    def time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.show)
        self.time_dialog.open()
    def show(self,instance,time):
    	self.sm.get_screen('ninput').ids[self.dynamic_ip].text = str(time)
    	self.fixedtimedict[self.dynamic_ip]=time
    
    def MainApp(self, *args):
    	self.stop()
    	MainApp.TestNavigationDrawer().run()
    
    def on_signup(self, *args):
        self.dialog.dismiss()
        self.sm.current = 'ninput'

    def show_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(title='[color=#FFFFFF]Confirmation[/color]',
                                   text='You have been registered.',
                                   size_hint=(0.4, 0.3),
                                   buttons=[
                                    MDFlatButton(text='CANCEL',
                                                 on_release=self.dialog_close,
                                                 text_color=self.theme_cls.primary_color),
                                    MDRaisedButton(text="OK!", 
                                                   on_release=self.on_signup,
                                                   text_color=self.theme_cls.primary_color)
                                   ])

        self.dialog.open()
        
    def checkpass(self, *args):
        self.inusedialog = MDDialog(title='[color=#FFFFFF]Username Incorrect[/color]',
                                    text='Your email is not registered!.',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.inusedialog_close,
                                                            text_color=self.theme_cls.primary_color)])

        self.inpasdialog = MDDialog(title='[color=#FFFFFF]Password Incorrect[/color]',
                                    text='You have entered the incorrect password.',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.inpasdialog_close,
                                                            text_color=self.theme_cls.primary_color)])
        
        self.val012=mysqllog.check(str(self.sm.get_screen('login').ids.username.text),str(self.sm.get_screen('login').ids.password.text))

        if self.val012==1:
            self.stop()
            MainApp.TestNavigationDrawer().run()

        elif self.val012==2:
            self.inpasdialog.open()

        elif self.val012==0:
            self.inusedialog.open()
        
    def dialog_close(self, *args):
        self.dialog.dismiss()

    def inusedialog_close(self, *args):
        self.inusedialog.dismiss()

    def inpasdialog_close(self, *args):
        self.inpasdialog.dismiss()

    def on_stop(self):
    	return True

if __name__ == '__main__':
    Test().run()