import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition

from kivy.config import Config
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'resizable', False)

old = 'ND'
curso = 'ND'

class MainScreen(ScreenManager):
	pass

class First(Screen):
	def btn1(self,instance):
		global old
		App.get_running_app().root.transition = SlideTransition(direction='left')
		App.get_running_app().root.current  = "second"
		#print(App.get_running_app().root.get_screen('first').ids['bt'].text)
		old = instance
	def btn1B(self,instance):
		global curso
		App.get_running_app().root.transition = SlideTransition(direction='right')
		App.get_running_app().root.current  = "third"	
		curso = instance

class Second(Screen):
	def btn2(self,instance):
		global old
		App.get_running_app().root.transition = SlideTransition(direction='right')
		App.get_running_app().root.current  = "first"
		old.text = instance.text
		
class Third(Screen):
	def btn3(self,instance):
		global curso
		App.get_running_app().root.transition = SlideTransition(direction='left')
		App.get_running_app().root.current  = "first"
		curso.text = App.get_running_app().root.ids.nuevo.text[:10]
		
	def btn3B(self,instance):
		App.get_running_app().root.transition = SlideTransition(direction='left')
		App.get_running_app().root.current  = "first"
		
		
class Tabla(GridLayout):
	def __init__(self,**kwargs):
		super(Tabla,self).__init__()
		self.cols = 4
		
		for i in range(1,21):
			self.Btns = Button(text=str(i))
			self.add_widget(self.Btns)
			self.Btns.bind(on_press = self.ret1_btn)
			
	def ret1_btn(self,instance):
		global value
		App.get_running_app().root.transition = SlideTransition(direction='right')
		App.get_running_app().root.current  = "first"
		#print(App.get_running_app().root.get_screen('first').ids['bt'].text)
		value = instance.text
		print(value)
	    
class Box02(BoxLayout):
	pass
		
class Box03(BoxLayout):
	def calculate(self,*arg):
		def asign(x):
			if(x == "Agregar"):
				return 0
			else:
				return int(x)
		a1 = asign(App.get_running_app().root.ids.n1.text)
		b1 = asign(App.get_running_app().root.ids.c1.text)
		a2 = asign(App.get_running_app().root.ids.n2.text)
		b2 = asign(App.get_running_app().root.ids.c2.text)
		a3 = asign(App.get_running_app().root.ids.n3.text)
		b3 = asign(App.get_running_app().root.ids.c3.text)
		a4 = asign(App.get_running_app().root.ids.n4.text)
		b4 = asign(App.get_running_app().root.ids.c4.text)
		a5 = asign(App.get_running_app().root.ids.n5.text)
		b5 = asign(App.get_running_app().root.ids.c5.text)
		
		if(a1*b1*a2*b2*a3*b3*a4*b4*a5*b5==0):
			res ='Datos inválidos'
		else: 
			res = format( (a1*b1+a2*b2+a3*b3+a4*b4+a5*b5)/(b1+b2+b3+b4+b5) ,'.2f')
		App.get_running_app().root.ids.prom.text = str(res)
		
class Box04(BoxLayout):
	pass
		
#value = self.ids
#								app.root.current = 'second'
#								app.root.transition.direction = "left"
#								print(value)
		# 					root.ids.n1.text = self.text
class Box05(BoxLayout):
	None

class MainApp(App): #mismo nombre de prom.kv
	title = "Calculadora de Promedios"
	def build(self):
		return MainScreen()

if __name__=='__main__':
	MainApp().run()
