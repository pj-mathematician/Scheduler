import os
import sys
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDTimePicker
if getattr(sys, "frozen", False):  
    os.environ["Scheduler-master"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["Scheduler-master"] = os.path.dirname(os.path.abspath(__file__))


KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "To-Do"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "todo"

            OneLineListItem:
                text: "Add/Delete"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "edit"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Scheduler"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "todo"
                MDFloatingActionButtonSpeedDial:
                    data: app.data
                	rotation_root_button: False
                MDLabel:
                    text: "MDDataTable"
                    halign: "center"
                MDFlatButton:
                    text: "Text"
                    on_release:
                        app.event_handler()

            Screen:
                name: "edit"

                MDLabel:
                    text: "edit here"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
class custom_events(FloatLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    data = {'delete':'Delete','pencil':'Add'}

#    def callback(self, instance, *args):
#        self.cstm_evnt = MDDialog(title='Custom Event',type='custom',content_cls=custom_events())
#        pass
            
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Main App/content.kv")
        return Builder.load_string(KV)

    cstm_evnt = None

    def event_handler(self):
        #self.time_dialog=MDTimePicker()
        if not self.cstm_evnt:
            self.cstm_evnt = MDDialog(
                                    title='[color=#FFFFFF]Custom Event[/color]',
                                    type='custom',
                                    content_cls=custom_events(),
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDFlatButton(text='CANCEL',
                                                          on_release=self.cstm_evnt_close,
                                                          text_color=self.theme_cls.primary_color),

                                    MDRaisedButton(text='OK',
                                                           on_release=self.cstm_evnt_close,
                                                           text_color=self.theme_cls.primary_color,),
                                    MDFillRoundFlatIconButton(text='Set',
                                                           icon='clock',
                                                           on_release=self.time_picker
                                                           )
                                                ])
                                                
        self.cstm_evnt.open()
    def time_picker(self, *args):        
        self.time_dialog=MDTimePicker()
        #self.time_dialog.bind(time=self.show)
        self.time_dialog.open()        
    def cstm_evnt_close(self,*args):
        self.cstm_evnt.dismiss()