#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from kivy.lang import Builder
from kivy.animation import Animation
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
email=''
if getattr(sys, "frozen", False):  
    os.environ["Scheduler-master"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["Scheduler-master"] = os.path.dirname(os.path.abspath(__file__))

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

        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Login_Signup/loginwindow.kv")
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Login_Signup/newinput.kv")
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Login_Signup/signupwindow.kv")

        self.sm = ScreenManager()
        self.sm.add_widget(loginwindow())
        self.sm.add_widget(signupwindow())
        self.sm.add_widget(newinput())

        return self.sm

    dialog = None
    inpasdialog=None
    inusedialog=None
    emptydialog=None
    alreadydialog=None
    sameemaildialog=None
    samepassdialog=None
    dynamic_ip=None
    val012=None
    previous_time = ObjectProperty()
    fixedtimedict={}

    def get_info(self):
        self.emptydialog = MDDialog(title='[color=#FFFFFF]Empty details[/color]',
                                    text='Please fill all the required details!',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.empty_close,
                                                            text_color=self.theme_cls.primary_color)])        
        self.alreadydialog = MDDialog(title='[color=#FFFFFF]Can not register![/color]',
                                    text='Email already exists!',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.already_close,
                                                            text_color=self.theme_cls.primary_color)])                                                    
        self.sameemaildialog = MDDialog(title='[color=#FFFFFF]Can not register![/color]',
                                    text='Email and Confirm email do not match!',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.sameemail_close,
                                                            text_color=self.theme_cls.primary_color)])        
        self.samepassdialog = MDDialog(title='[color=#FFFFFF]Can not register![/color]',
                                    text='Password and Confirm password do not match!',
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDRaisedButton(text='OK',
                                                            on_release=self.samepass_close,
                                                            text_color=self.theme_cls.primary_color)]) 

        name = str(self.sm.get_screen('signup').ids.name.text)
        email = str(self.sm.get_screen('signup').ids.email.text)
        self.mainemail=email
        confirm_email = str(self.sm.get_screen('signup').ids.confirm_email.text)
        password = str(self.sm.get_screen('signup').ids.password.text)
        confirm_pass = str(self.sm.get_screen('signup').ids.confirm_password.text)

        if name=='' or email=='' or confirm_email=='' or password=='' or confirm_pass=='':
            self.emptydialog.open()

        elif email!=confirm_email:
            self.sameemaildialog.open()

        elif password!=confirm_pass:
            self.samepassdialog.open()

        elif mysqllog.check(email,password)==1 or mysqllog.check(email,password)==2:

            self.alreadydialog.open()
        else:
            mysqllog.add_new_user([email, password])
            self.show_dialog()


    def time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.show)
        self.time_dialog.open()

    def show(self,instance,time):
    	self.sm.get_screen('ninput').ids[self.dynamic_ip].text = str(time)
    	mysqllog.add_user_data(self.mainemail,[(str(self.dynamic_ip),str(time))])
    	self.fixedtimedict[self.dynamic_ip]=time
    
    def MainApp(self, *args):
    	self.stop()
    	MainApp.TestNavigationDrawer().run()

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
        


    def on_stop(self):
    	return True
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
            self.mainemail=str(self.sm.get_screen('login').ids.username.text
            MainApp.email=str(self.sm.get_screen('login').ids.username.text
            MainApp.TestNavigationDrawer().run()

        elif self.val012==2:
            self.inpasdialog.open()

        elif self.val012==0:
            self.inusedialog.open()
            
    def check_focus(self, instance, text):
        if not text:
            self.sm.get_screen('signup').ids[self.ip2].helper_text= 'Re-Enter your {}!'.format(self.ip1)
            return
        if text != self.sm.get_screen('signup').ids[self.ip1].text:
            self.sm.get_screen('signup').ids[self.ip2].helper_text='{} does not match!'.format(self.ip1)
            instance.error = True
            Animation(
                duration=0.2, _current_error_color=instance.error_color
            ).start(instance)
            Animation(
                duration=0.2,
                _current_line_color=instance.error_color,
                _current_hint_text_color=instance.error_color,
                _current_right_lbl_color=instance.error_color,
            ).start(instance)
        else:
            self.sm.get_screen('signup').ids[self.ip2].helper_text='Re-Enter your {}!'.format(self.ip1)
            Animation(
                duration=0.2, _current_error_color=(0, 0, 0, 0)
            ).start(instance)
            Animation(
                duration=0.2,
                _current_line_color=instance.line_color_focus,
                _current_hint_text_color=instance.line_color_focus,
                _current_right_lbl_color=instance.line_color_focus,
            ).start(instance)
            instance.error = False

        
    def dialog_close(self, *args):
        self.dialog.dismiss()

    def inusedialog_close(self, *args):
        self.inusedialog.dismiss()

    def inpasdialog_close(self, *args):
        self.inpasdialog.dismiss()
    
    def empty_close(self, *args):
        self.emptydialog.dismiss()
        
    def already_close(self, *args):
        self.alreadydialog.dismiss()

    def sameemail_close(self, *args):
        self.sameemaildialog.dismiss()                

    def samepass_close(self, *args):
        self.samepassdialog.dismiss()
    def on_stop(self):
    	return True
    
    def on_signup(self, *args):
        self.dialog.dismiss()
        self.sm.current = 'ninput'    

if __name__ == '__main__':
    Test().run()
