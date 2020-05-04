from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

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


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    data = {'delete':'Delete','pencil':'Add'}
    
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Builder.load_string(KV)

#TestNavigationDrawer().run()
	