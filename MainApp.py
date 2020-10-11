import os
import sys
import time
from operator import itemgetter
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.card import MDCardSwipe
if getattr(sys, "frozen", False):  
    os.environ["Scheduler-master"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["Scheduler-master"] = os.path.dirname(os.path.abspath(__file__))
def i2t(instance):
	return instance.text2

KV = '''
<SwipeToDeleteItem>:
    anchor:'right'
    type_swipe: 'auto'
    size_hint_y: None
    height: content.height
    on_swipe_complete:app.remove_item(root)

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": 0.5}
            on_release: app.remove_item(root)

    MDCardSwipeFrontBox:

        TwoLineListItem:
            id: content
            text: root.text
            secondary_text: root.text2
            _no_ripple_effect: True


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
	


    NavigationLayout:
        #x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "todo"
                BoxLayout:
                	orientation: "vertical"
                	spacing: "10dp"
				    MDToolbar:
				        id: toolbar
				        pos_hint: {"top": 1}
				        elevation: 10
				        title: "Scheduler"
				        left_action_items: []
				        right_action_items:[["plus", lambda x: app.add()],["refresh", lambda x: app.refresh_callback()]]                
	
                

	                ScrollView:
	          
	                	MDList:
	                		id:md_list
	                		padding: "2dp"
	                	


            Screen:
                name: "edit"

                MDLabel:
                    text: "edit here"
                    halign: "center"
                MDFloatingActionButtonSpeedDial:
                    data: app.data
                   # on_release:
                   #	app.event_handler()
                	rotation_root_button: False
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
class custom_events(BoxLayout):
   pass
   
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    text2 = StringProperty()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    temp_instance=None
    main_event_list=[]
    my_event=None
    mytime=None
    data = {'delete':'Delete','pencil':'Add'}

#    def callback(self, instance, *args):
#        self.cstm_evnt = MDDialog(title='Custom Event',type='custom',content_cls=custom_events())
#        pass
            
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Main App/content.kv")
        
        return Builder.load_string(KV)
        self.refresh_callback()
        

    cstm_evnt = None
    dlt_event= None


    def add(self):
        #self.time_dialog=MDTimePicker()
        if not self.cstm_evnt:
            self.cstm_evnt = MDDialog(
                                    
                                    title='[color=#FFFFFF]Add Event[/color]',
                                    type='custom',
                                    content_cls=custom_events(),
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDFlatButton(text='CANCEL',
                                                          on_release=self.cstm_evnt_close,
                                                          text_color=self.theme_cls.primary_color),
                                    MDFillRoundFlatIconButton(text='Set Time',
                                                           icon='clock',
                                                           on_release=self.time_picker
                                                           )
                                                ])
                                                
        self.cstm_evnt.open()
    def time_picker(self, *args):        
        self.time_dialog=MDTimePicker()
        #self.time_dialog.title=self.my_event
        self.time_dialog.bind(time=self.show)
        self.time_dialog.open()
        self.cstm_evnt.dismiss()
        self.cstm_event=None
    #confirmd=None
    
    def confirm(self):
    	if not self.confirmd:
    		self.confirmd=MDDialog(title='[color=#FFFFFF]Confirm[/color]',size_hint=(0.4, 0.3),text="Add Event {} at {} ?".format(self.my_event,self.mytime),buttons=[MDFlatButton(text='NO',
                                                          on_release=self.clconfirmd,
                                                          text_color=self.theme_cls.primary_color),
                                    MDRaisedButton(text='YES',
                                                           on_release=self.event_adder
                                                           )
                                                ])
    		self.confirmd.open()
    def clconfirmd(self,*args):
    	self.confirmd.dismiss()
    	
    def refresh_callback(self, *args):
        self.main_event_list=sorted(self.main_event_list,key=itemgetter(1))
        self.root.ids.md_list.clear_widgets()
        for i in self.main_event_list:
        	self.root.ids.md_list.add_widget(SwipeToDeleteItem(text=i[0],text2=i[1]))
        	#self.root.ids.md_list.add_widget(i)
    def textfrominstance(self,instance):
        	return instance.text
        	
    def show(self,instance,time):
        self.mytime=time
        self.confirmd=None
        self.confirm()
        #fixedtimedict[key]=time
    def cstm_evnt_close(self,*args):
        self.cstm_evnt.dismiss()
        
    def remove_item(self,instance):
        print(instance.text)
        self.temp_instance=instance
        if not self.dlt_event:
    	    self.dlt_event=MDDialog(title='[color=#FFFFFF]Confirm Delete[/color]',size_hint=(0.4, 0.3),text="Delete {}?".format(instance.text),buttons=[MDFlatButton(text='NO',on_release=self.cldelevent,text_color=self.theme_cls.primary_color),MDRaisedButton(text='YES',on_press=self.rem)])
    	    self.dlt_event.open()
    def rem(self,instance):
    	print(self.main_event_list)
    	self.dlt_event.dismiss()
    	self.root.ids.md_list.remove_widget(self.temp_instance)
    	for i in range(len(self.main_event_list)):
    		if self.main_event_list[i][0]==self.temp_instance.text:
    			del(self.main_event_list[i])
    			print(self.main_event_list)
    			break
    	self.dlt_event=None
    	
    def cldelevent(self,instance):
    	self.dlt_event.dismiss()
    def event_adder(self,instance):
    	self.confirmd.dismiss()
    	
    	instance=SwipeToDeleteItem(text=self.my_event,text2=str(self.mytime))
    	self.main_event_list.append((instance.text,instance.text2))
    	self.root.ids.md_list.add_widget(instance)
if __name__ == "__main__":         
    TestNavigationDrawer().run()
