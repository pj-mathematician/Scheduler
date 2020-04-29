#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from datetime import datetime
from datetime import time
from datetime import date
from kivy.properties import ObjectProperty
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
        Builder.load_file(kv2)
        self.sm = ScreenManager()
        self.sm.add_widget(loginwindow())
        self.sm.add_widget(signupwindow())
        self.sm.add_widget(newinput())
        return self.sm

    dialog = None
    previous_time = ObjectProperty()


    def show_time_picker(self, *args):
        from kivymd.uix.picker import MDTimePicker
        self.time_dialog=MDTimePicker()
        self.time_dialog.bind(time=self.get_time)
        self.time_dialog.open()

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
    def get_time(self, instance, time, **kwargs):
    	super(Test, self).__init__(**kwargs)
    	self.ids.wake.text = str(time)
    	self.previous_time = time


if __name__ == '__main__':
    Test().run()
