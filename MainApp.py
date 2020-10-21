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
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCardSwipe
import mysqllog
from Logic import mintohhmmss
if getattr(sys, "frozen", False):  
    os.environ["Scheduler-master"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["Scheduler-master"] = os.path.dirname(os.path.abspath(__file__))
def i2t(instance):
	return instance.text2

email='Test@gmail.com'
KV = '''
<SwipeToDeleteItem>:
    anchor:'right'
    type_swipe: 'auto'
    size_hint_y: None
    height: content.height
    on_swipe_complete:app.remove_item(root)
    
    MDCardSwipeFrontBox:
        TwoLineListItem:
            id: content
            text: root.text
            secondary_text: root.text2
            _no_ripple_effect: True

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
				        right_action_items:[["plus", lambda x: app.add()],["briefcase-plus", lambda x: app.addM()],["refresh", lambda x: app.refresh_callback()],["trash-can", lambda x:app.delete()]]                
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
'''
class custom_events(BoxLayout):
   pass
class custom_events2(BoxLayout):
   pass
class custom_events3(BoxLayout):
   pass
   
class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    text2 = StringProperty()
    
class TestNavigationDrawer(MDApp):
    main_text=''
    temp_instance=None
    main_event_list=[]
    main_meeting_list=[]
    main=[]
    my_event=None
    mytime=None
    starttime=None
    endtime=None
    data = {'delete':'Delete','pencil':'Add'}
    	

#    def callback(self, instance, *args):
#        self.cstm_evnt = MDDialog(title='Custom Event',type='custom',content_cls=custom_events())
#        pass
            
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Main App/content.kv")
        Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Main App/content2.kv")
        #Builder.load_file(f"{os.environ['Scheduler-master']}/KivyFiles/Main App/content3.kv")
        return Builder.load_string(KV)
        #self.refresh_callback()
    def on_start(self):
        self.load_schedule()
    
        
    def load_schedule(self):
    	for i in mysqllog.return_schedule(email):
    		starttime=mintohhmmss(i[0])
    		endtime=mintohhmmss(i[1])
    		evnt=i[2]
    		self.main.append((evnt,starttime,endtime))
    		instance=SwipeToDeleteItem(text=evnt,text2=starttime+' - '+endtime)
    		self.root.ids.md_list.add_widget(instance)
    	
    cstm_evnt = None
    cstm_evnt2=None
    confirmd2=None
    confirmdf=None
    deleteb=None
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
    def addM(self):
        #self.time_dialog=MDTimePicker()
        if not self.cstm_evnt2:
            self.cstm_evnt2 = MDDialog(
                                    
                                    title='[color=#FFFFFF]Add Meeting[/color]',
                                    type='custom',
                                    content_cls=custom_events2(),
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDFlatButton(text='CANCEL',
                                                          on_release=self.cstm_evnt_close2,
                                                          text_color=self.theme_cls.primary_color),
                                    MDFillRoundFlatIconButton(text='Starting Time',
                                                           icon='clock',
                                                           on_release=self.time_picker2
                                                           )  
                                                ])
                                                
        self.cstm_evnt2.open()
    def delete(self):
        #self.time_dialog=MDTimePicker()
        if not self.cstm_evnt2:
            self.cstm_evnt2 = MDDialog(
                                    
                                    title='[color=#FFFFFF]Delete[/color]',
                                    type='custom',
                                    content_cls=custom_events2(),
                                    size_hint=(0.4, 0.3),
                                    buttons=[MDFlatButton(text='CANCEL',
                                                          on_release=self.cstm_evnt_close2,
                                                          text_color=self.theme_cls.primary_color),
                                    MDRaisedButton(text='Delete',
                                                           on_release=self.deleteevent
                                                           )  
                                                ])
                                                
        self.cstm_evnt2.open()
    def deleteevent(self):
    	for i in self.ids.md_list:
    		if str(i.text)==self.my_event:
    			self.ids.md_list.remove_widget(i)
    	try:
    	   mysqllog.remove_routine(email,self.my_event)
    	except:
    		mysqllog.remove_user_data(email,self.my_event)    				
    def time_picker(self, *args):        
        self.time_dialog=MDTimePicker()
        #self.time_dialog.title=self.my_event
        self.time_dialog.bind(time=self.show)
        self.time_dialog.open()
        self.cstm_evnt.dismiss()
        self.cstm_event=None
    #confirmd=None
    def time_picker2(self, *args):        
        self.time_dialog=MDTimePicker()
        #self.time_dialog.title=self.my_event
        self.time_dialog.bind(time=self.show2)
        self.time_dialog.open()
        self.cstm_evnt2.dismiss()
        self.cstm_event2=None
    def time_picker3(self, *args):        
        self.time_dialog=MDTimePicker()
        #self.time_dialog.title=self.my_event
        self.time_dialog.bind(time=self.show3)
        self.time_dialog.open()
        self.confirmd2.dismiss()
    def show2(self,instance,time):
        self.starttime=time
        print(self.starttime)
        self.confirmd2=None
        self.confirm2()
    def show3(self,instance,time):
        self.endtime=time
        print(self.endtime)
        self.confirmdf=None
        self.confirmfinal()
    def delete_callback(self):
        pass
        
    def confirm2(self):
    	if not self.confirmd2:
    		self.confirmd2=MDDialog(title='[color=#FFFFFF]Confirm[/color]',size_hint=(0.4, 0.3),text="{},{}".format(self.my_event,self.starttime),buttons=[MDFlatButton(text='Cancel',
                                                          on_release=self.clconfirmd2,
                                                          text_color=self.theme_cls.primary_color),
                                    MDFillRoundFlatIconButton(text='Ending Time',
                                                           icon='clock',
                                                           on_release=self.time_picker3
                                                           ) 
                                                ])
    		self.confirmd2.open()
    def confirmfinal(self):
    	if not self.confirmdf:
    		self.confirmdf=MDDialog(title='[color=#FFFFFF]Confirm[/color]',size_hint=(0.4, 0.3),text="Add Meeting {} at {} to {}?".format(self.my_event,self.starttime,self.endtime),buttons=[MDFlatButton(text='NO',
                                                          on_release=self.clconfirmdf,
                                                          text_color=self.theme_cls.primary_color),
                                    MDRaisedButton(text='YES',
                                                           on_release=self.event_adder2
                                                           )
                                                ])
    		self.confirmdf.open()

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
    def deletecl(self,*args):
    	self.deleteb.dismiss()
    def clconfirmd(self,*args):
    	self.confirmd.dismiss()
    def clconfirmd2(self,*args):
    	self.confirmd2.dismiss()
    def clconfirmdf(self,*args):
    	self.confirmdf.dismiss()
    def refresh_callback(self, *args):
        mysqllog.add_routine('Test@gmail.com',self.main_meeting_list)
        mysqllog.add_user_data('Test@gmail.com',self.main_event_list)
        self.main=sorted(self.main,key=itemgetter(1))
        self.root.ids.md_list.clear_widgets()
        for i in self.main:
        	if len(i)==2:
        		self.root.ids.md_list.add_widget(SwipeToDeleteItem(text=i[0],text2=i[1]))
        	else:
        		self.root.ids.md_list.add_widget(SwipeToDeleteItem(text=i[0],text2=i[1]+' - '+i[2]))
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
    def cstm_evnt_close2(self,*args):
        self.cstm_evnt2.dismiss()        
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
    	self.main.append((str(self.my_event),str(self.mytime)))
    	self.root.ids.md_list.add_widget(instance)
    	mysqllog.add_user_data(email,[(self.my_event,self.mytime)])
    def event_adder2(self,instance):
    	self.confirmdf.dismiss()
    	
    	instance=SwipeToDeleteItem(text=self.my_event,text2=str(self.starttime)+' - '+str(self.endtime))
    	self.main_meeting_list.append((str(self.my_event),str(self.starttime),str(self.endtime)))
    	self.main.append((str(self.my_event),str(self.starttime),str(self.endtime)))
    	self.root.ids.md_list.add_widget(instance)
    	mysqllog.add_routine(email,[(self.my_event,self.starttime,self.endtime)])

if __name__ == "__main__":         
    TestNavigationDrawer().run()
