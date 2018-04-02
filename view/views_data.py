import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label

import matplotlib.pyplot as plt

# Window.size = (1284, 640)
# Window.top = 100
# Window.left = 100


class BodyLayout(GridLayout):
    def on_create(self):
        self.data = {}
        self.data['pipe'] = '1'
        self.data['temp1'] = 0
        self.data['temp2'] = 0
        self.data['hum1'] = 0
        self.data['hum2'] = 0
        self.data['press'] = 0
        self.data['temp_sr'] = 0
        self.data['hum_sr'] = 0

        self.label1 = self.ids.label1

        self.a1_t1 = self.ids.a1_t1
        self.a1_t2 = self.ids.a1_t2
        self.a1_h1 = self.ids.a1_h1
        self.a1_h2 = self.ids.a1_h2
        self.a1_p = self.ids.a1_p

        self.a2_t1 = self.ids.a2_t1
        self.a2_t2 = self.ids.a2_t2
        self.a2_h1 = self.ids.a2_h1
        self.a2_h2 = self.ids.a2_h2
        self.a2_p = self.ids.a2_p

        self.a3_t1 = self.ids.a3_t1
        self.a3_t2 = self.ids.a3_t2
        self.a3_h1 = self.ids.a3_h1
        self.a3_h2 = self.ids.a3_h2
        self.a3_p = self.ids.a3_p
	
        self.a4_t1 = self.ids.a4_t1
        self.a4_t2 = self.ids.a4_t2
        self.a4_h1 = self.ids.a4_h1
        self.a4_h2 = self.ids.a4_h2
        self.a4_p = self.ids.a4_p
	
        self.a5_t1 = self.ids.a5_t1
        self.a5_t2 = self.ids.a5_t2
        self.a5_h1 = self.ids.a5_h1
        self.a5_h2 = self.ids.a5_h2
        self.a5_p = self.ids.a5_p

        self.a1_t1.data_datch = "Modul 1 TEMP 1:"
        self.a1_t2.data_datch = "Modul 1 TEMP 2:"
        self.a1_h1.data_datch = "Modul 1 HUMI 1:"
        self.a1_h2.data_datch = "Modul 1 HUMI 2:"
        self.a1_p.data_datch = "Modul 1 PRES:"

        self.a2_t1.data_datch = "Modul 2 TEMP 1:"
        self.a2_t2.data_datch = "Modul 2 TEMP 2:"
        self.a2_h1.data_datch = "Modul 2 HUMI 1:"
        self.a2_h2.data_datch = "Modul 2 HUMI 2:"
        self.a2_p.data_datch = "Modul 2 PRES:"

        self.a3_t1.data_datch = "Modul 3 TEMP 1:"
        self.a3_t2.data_datch = "Modul 3 TEMP 2:"
        self.a3_h1.data_datch = "Modul 3 HUMI 1:"
        self.a3_h2.data_datch = "Modul 3 HUMI 2:"
        self.a3_p.data_datch = "Modul 3 PRES:"

        self.a4_t1.data_datch = "Modul 4 TEMP 1:"
        self.a4_t2.data_datch = "Modul 4 TEMP 2:"
        self.a4_h1.data_datch = "Modul 4 HUMI 1:"
        self.a4_h2.data_datch = "Modul 4 HUMI 2:"
        self.a4_p.data_datch = "Modul 4 PRES:"

        self.a5_t1.data_datch = "Modul 5 TEMP 1:"
        self.a5_t2.data_datch = "Modul 5 TEMP 2:"
        self.a5_h1.data_datch = "Modul 5 HUMI 1:"
        self.a5_h2.data_datch = "Modul 5 HUMI 2:"
        self.a5_p.data_datch = "Modul 5 PRES:"

        

        self.label1.on_press = self.call_moadal

        self.a1_t1.bind(on_press=self.call_modal_item)
        self.a1_t2.bind(on_press=self.call_modal_item)
        self.a1_h1.bind(on_press=self.call_modal_item)
        self.a1_h2.bind(on_press=self.call_modal_item)
        self.a1_p.bind(on_press=self.call_modal_item)

        self.a2_t1.bind(on_press=self.call_modal_item)
        self.a2_t2.bind(on_press=self.call_modal_item)
        self.a2_h1.bind(on_press=self.call_modal_item)
        self.a2_h2.bind(on_press=self.call_modal_item)
        self.a2_p.bind(on_press=self.call_modal_item)

        self.a3_t1.bind(on_press=self.call_modal_item)
        self.a3_t2.bind(on_press=self.call_modal_item)
        self.a3_h1.bind(on_press=self.call_modal_item)
        self.a3_h2.bind(on_press=self.call_modal_item)
        self.a3_p.bind(on_press=self.call_modal_item)

        self.a4_t1.bind(on_press=self.call_modal_item)
        self.a4_t2.bind(on_press=self.call_modal_item)
        self.a4_h1.bind(on_press=self.call_modal_item)
        self.a4_h2.bind(on_press=self.call_modal_item)
        self.a4_p.bind(on_press=self.call_modal_item)

        self.a5_t1.bind(on_press=self.call_modal_item)
        self.a5_t2.bind(on_press=self.call_modal_item)
        self.a5_h1.bind(on_press=self.call_modal_item)
        self.a5_h2.bind(on_press=self.call_modal_item)
        self.a5_p.bind(on_press=self.call_modal_item)

        Clock.schedule_interval(self.timer, 0.01)

    def timer(self, dt):
       
        if self.data['pipe'] == '1':
            self.a1_t1.text = str(self.data['temp1']) + " °C"
            self.a1_t2.text = str(self.data['temp2']) + " °C"
            self.a1_h1.text = str(self.data['hum1'])   + " %"
            self.a1_h2.text = str(self.data['hum2']) + " %"
            self.a1_p.text = str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '2':
            self.a2_t1.text = str(self.data['temp1']) + " °C"
            self.a2_t2.text = str(self.data['temp2']) + " °C"
            self.a2_h1.text = str(self.data['hum1'])   + " %"
            self.a2_h2.text = str(self.data['hum2']) + " %"
            self.a2_p.text = str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '3':
            self.a3_t1.text = str(self.data['temp1']) + " °C"
            self.a3_t2.text = str(self.data['temp2']) + " °C"
            self.a3_h1.text = str(self.data['hum1'])   + " %"
            self.a3_h2.text = str(self.data['hum2']) + " %"
            self.a3_p.text = str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '4':
            self.a4_t1.text = str(self.data['temp1']) + " °C"
            self.a4_t2.text = str(self.data['temp2']) + " °C"
            self.a4_h1.text = str(self.data['hum1'])   + " %"
            self.a4_h2.text = str(self.data['hum2']) + " %"
            self.a4_p.text = str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '5':
            self.a5_t1.text = str(self.data['temp1']) + " °C"
            self.a5_t2.text = str(self.data['temp2']) + " °C"
            self.a5_h1.text = str(self.data['hum1'])   + " %"
            self.a5_h2.text = str(self.data['hum2']) + " %"
            self.a5_p.text = str(self.data['press']) + " Pa"


    def call_moadal(self):

        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()
        text1 = "TEMP: {0} °C".format(self.data['temp_sr'])
        text2 = "HUMI: {0} %".format(self.data['hum_sr'])
        popup = ModalView(size_hint=(0.75, 0.6))
        layout = BoxLayout(orientation='vertical')

        tem_label = MyLabel(text=text1, font_size=70, color=[1, 1, 0, 1])
        hum_label = MyLabel(text=text2, font_size=70, color=[0.5, 0.5, 1, 1])


        layout.add_widget(tem_label)
        layout.add_widget(hum_label)
        popup.add_widget(layout)
        popup.bind()
        popup.open()

    def call_modal_item(self, btn):
        text1 = btn.data_datch
        text2 = btn.text
        popup = ModalView(size_hint=(0.5, 0.5))
        layout = BoxLayout(orientation='vertical')

        tem_label = MyLabel(text=text1, font_size=40, color=[1, 1, 0, 1], size_hint=(1, None))
        hum_label = MyLabel(text=text2, font_size=70, color=[0.5, 0.5, 1, 1])

        layout.add_widget(tem_label)
        layout.add_widget(hum_label)
        popup.add_widget(layout)
        popup.bind()
        popup.open()


class MyLabel(Label):
   pass
        

class BodyLayoutApp(App):
    title = "Green House"
    layout = BodyLayout
    def build(self):
        self.layout = BodyLayout()
        self.layout.on_create()
        Clock.schedule_interval(self.layout.timer, 0.01)
        return self.layout

    def set_data(self, data):
        self.layout.data = data

    

if __name__ == '__main__':
     BodyLayoutApp().run()