# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:58:37 2018

@author: Sandman
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.button import Button
#from kivy.uix.dropdown import DropDown
#from kivy.uix.button import Button
#from kivy.base import runTouchApp

#class HCC(GridLayout):
#    pass

class StartScreen(Screen):
    pass

class LogInScreen(Screen):
    pass

class RootScreen(ScreenManager):
    pass

class GameSched(Widget):
    pass

class HCCApp(App):
    def build(self):
        self.title = 'Holy City Classic 2019'
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='Start'))
        sm.add_widget(LogInScreen(name='Login'))
        return sm
    
if __name__ == '__main__':
    HCCApp().run()