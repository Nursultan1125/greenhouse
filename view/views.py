import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
 
# A page layout is used to create multi-page layouts
# that you can flip through
 
class PageLayoutApp(App):
    
 
    def build(self):
        pl = PageLayout()

        self.a1_t1 = pl.ids.a1_t1
        self.a1_t2 = pl.ids.a1_t2
        self.a1_h1 = pl.ids.a1_h1
        self.a1_h2 = pl.ids.a1_h2
        self.a1_p = pl.ids.a1_p

        self.a2_t1 = pl.ids.a2_t1
        self.a2_t2 = pl.ids.a2_t2
        self.a2_h1 = pl.ids.a2_h1
        self.a2_h2 = pl.ids.a2_h2
        self.a2_p = pl.ids.a2_p

        self.a3_t1 = pl.ids.a3_t1
        self.a3_t2 = pl.ids.a3_t2
        self.a3_h1 = pl.ids.a3_h1
        self.a3_h2 = pl.ids.a3_h2
        self.a3_p = pl.ids.a3_p
	
        self.a4_t1 = pl.ids.a4_t1
        self.a4_t2 = pl.ids.a4_t2
        self.a4_h1 = pl.ids.a4_h1
        self.a4_h2 = pl.ids.a4_h2
        self.a4_p = pl.ids.a4_p
	
        self.a5_t1 = pl.ids.a5_t1
        self.a5_t2 = pl.ids.a5_t2
        self.a5_h1 = pl.ids.a5_h1
        self.a5_h2 = pl.ids.a5_h2
        self.a5_p = pl.ids.a5_p

        self.data = {}
        self.data['pipe'] = 0
        self.data['temp1'] = 0
        self.data['temp2'] = 0
        self.data['hum1'] = 0
        self.data['hum2'] = 0
        self.data['press'] = 0
        Clock.schedule_interval(self.timer, 0.01)
        return pl
    
    def timer(self, dt):
        temp1 = "Temperature1: "
        temp2 = "Temperature2: "
        hum1 = "Humidity1: "
        hum2 = "Humidity2: "
        press = "Pressure: "
        if self.data['pipe'] == '1':
            self.a1_t1.text = temp1 + str(self.data['temp1']) + " °C"
            self.a1_t2.text = temp2 + str(self.data['temp2']) + " °C"
            self.a1_h1.text = hum1 + str(self.data['hum1'])   + " %"
            self.a1_h2.text = hum2 + str(self.data['hum2']) + " %"
            self.a1_p.text = press + str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '2':
            self.a2_t1.text = temp1 + str(self.data['temp1']) + " °C"
            self.a2_t2.text = temp2 + str(self.data['temp2']) + " °C"
            self.a2_h1.text = hum1 + str(self.data['hum1'])   + " %"
            self.a2_h2.text = hum2 + str(self.data['hum2']) + " %"
            self.a2_p.text = press + str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '3':
            self.a3_t1.text = temp1 + str(self.data['temp1']) + " °C"
            self.a3_t2.text = temp2 + str(self.data['temp2']) + " °C"
            self.a3_h1.text = hum1 + str(self.data['hum1'])   + " %"
            self.a3_h2.text = hum2 + str(self.data['hum2']) + " %"
            self.a3_p.text = press + str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '4':
            self.a4_t1.text = temp1 + str(self.data['temp1']) + " °C"
            self.a4_t2.text = temp2 + str(self.data['temp2']) + " °C"
            self.a4_h1.text = hum1 + str(self.data['hum1'])   + " %"
            self.a4_h2.text = hum2 + str(self.data['hum2']) + " %"
            self.a4_p.text = press + str(self.data['press']) + " Pa"
        elif self.data['pipe'] == '5':
            self.a5_t1.text = temp1 + str(self.data['temp1']) + " °C"
            self.a5_t2.text = temp2 + str(self.data['temp2']) + " °C"
            self.a5_h1.text = hum1 + str(self.data['hum1'])   + " %"
            self.a5_h2.text = hum2 + str(self.data['hum2']) + " %"
            self.a5_p.text = press + str(self.data['press']) + " Pa"
 


