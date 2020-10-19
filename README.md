# Scheduler
Scheduler made in Kivy language using kivyMD library.
KivyMD - https://github.com/kivymd/KivyMD

Note:-

1) We are still continuing with the offline server due to some issues we couldn't resolve in the online one

2) Made the signup page functional. 

3) Shortcut present in main.py is only for the developers. It is NOT meant for the normal user. 

# Info for adding functions in MainApp.py
-> event_adder(self,instance):

    adds the event
  
    instance.text is the event name being added
  
    instance.text2 is the time string being added 
  

-> rem(self,instance):

    removes the event
  
    temp_instance.text is the event name
  
    temp_instance.text2 is the time string
  

-> refresh_callback(self,\* args)

    its main use is to sort the event list.
  
  
-> Note:
    Instead of passing sql queries every time an element is updated, We use main_event_list which contains list of tuples containing event name and time(can be considered as a temp data loaded inside the code). After you simply append the stuff in the list and use the refresh_callback() the gui will get updated.
