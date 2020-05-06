from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
kv1='content.kv'
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
class custom_events(BoxLayout):
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
        self.theme_cls.theme_style = 'Light'
        Builder.load_file(kv1)
        return Builder.load_string(KV)

    cstm_evnt = None

    def event_handler(self):
        if not self.cstm_evnt:
            self.cstm_evnt = MDDialog(
                                    title='Custom Event',
                                    type='custom',
                                    content_cls=custom_events(),
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDFlatButton(text='OK',on_release=self.cstm_evnt_close)]
                                    )
        self.cstm_evnt.open()
    def cstm_evnt_close(self,*args):
        self.cstm_evnt.dismiss()

TestNavigationDrawer().run()
	