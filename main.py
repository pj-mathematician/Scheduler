#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from datetime import time
from datetime import date
from kivy.properties import ObjectProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDTimePicker


kv1 = 'Login.kv'
kv2 = 'newinput.kv'


class loginwindow(Screen):
    pass


class signupwindow(Screen):
    pass


class newinput(Screen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file(kv1)
        self.sm = ScreenManager()
        self.sm.add_widget(loginwindow())
        self.sm.add_widget(signupwindow())
        self.sm.add_widget(newinput())
        return self.sm

    dialog = None
    previous_time = ObjectProperty()

    fixedtimedict={}
###***HIGHLY INEFFICIENT****###
    def wake_time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.wake_time)
        self.time_dialog.open()
    
    def bkf_time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.bkf_time)
        self.time_dialog.open()
    
    def lch_time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.lch_time)
        self.time_dialog.open()
    
    def din_time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.din_time)
        self.time_dialog.open()    
    
    def slp_time_picker(self):        
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.slp_time)
        self.time_dialog.open()
    
    def wake_time(self, instance, time):
    	
    	self.sm.get_screen('ninput').ids.wake.text = str(time)
    	self.previous_time = time
    	self.fixedtimedict['wake']=time
    
    def bkf_time(self, instance, time):
    	
    	self.sm.get_screen('ninput').ids.bkf.text = str(time)
    	self.previous_time = time
    	self.fixedtimedict['bkf']=time    

    def lch_time(self, instance, time):
    	
    	self.sm.get_screen('ninput').ids.lch.text = str(time)
    	self.previous_time = time
    	self.fixedtimedict['lch']=time            
    
    def din_time(self, instance, time):
    	
    	self.sm.get_screen('ninput').ids.din.text = str(time)
    	self.previous_time = time
    	self.fixedtimedict['din']=time        
    
    def slp_time(self, instance, time):
    	
    	self.sm.get_screen('ninput').ids.slp.text = str(time)
    	self.previous_time = time
    	self.fixedtimedict['slp']=time        
#####UGLY STUFF OVER!#####    
    

    def on_signup(self, *args):
        self.sm.current = 'ninput'

    def show_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(title='Confirmation',
                                   text='You have been registered.',
                                   size_hint=(0.7, 0.3),
                                   text_button_ok='OK',
                                   events_callback=self.on_signup)

        self.dialog.open()


if __name__ == '__main__':
    Test().run()
