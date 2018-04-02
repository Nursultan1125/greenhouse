#!/usr/bin/python
from numpy.ma import arange

import database.sqlite3con
from config import PORT_NAME, COUNT_READ_DATA
from database.mysqlcon import DBHelper
from connect_serial.serial_connect import SerialConnectArduino
import datetime
import threading


import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

from view.views_data import BodyLayoutApp
# from view.views import PageLayoutApp

glob_data = {'pipe': 1}

def line_str(result):
    res_text = ""
    for key in result:
        res_text += "{0}: {1}".format(key, str(result[key])).ljust(22, ' ')
    return res_text

data_counter = dict()


def main():
    global glob_data
    arduino = SerialConnectArduino(port=PORT_NAME)
    try:
        db = DBHelper()
    except:
        print("Error Mysql!!! ")
        print("connect sqlite3 ")
        db = database.sqlite3con.DBHelper()
    # print(1, len(db.select_pipe(1)))
    # print(2, len(db.select_pipe(2)))
    # print(3, len(db.select_pipe(3)))
    # print(4, len(db.select_pipe(4)))
    # print(5, len(db.select_pipe(5)))



    while True:
        dt = datetime.datetime.now()
        try:
            data = arduino.readline()
            if len(data) > 6:
                pipe = str(data['pipe'])
                if pipe in data_counter:
                    data_counter[pipe] += 1
                else:
                    data_counter.update({pipe: 1})
                print(data_counter)
                for key in data_counter:
                    if data_counter[key] >= COUNT_READ_DATA:
                        data['datatime'] = dt.strftime('%Y-%M-%d %H:%m:%S')
                        db.insert_db(data['pipe'], data['temp1'], data['hum1'], data['temp2'], data['hum2'],
                                     data['press'])
                        data_counter[key] = 0

                        print(line_str(data))

                data['datatime'] = dt.strftime('%Y-%M-%d %H:%m:%S')
                glob_data = data


        except KeyboardInterrupt:
            print("\nExit !!!")
            break

app = BodyLayoutApp()
switch = False


def d():
    app.run()




    
    
if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=d)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t2.start()
    t1.start()
    
    while True:
        t1, t2, h1, h2 = 0, 0, 0, 0
        if 'temp1' in glob_data:
            t1 = float(glob_data['temp1'])
            t2 = float(glob_data['temp2'])

            h1 = float(glob_data['hum1'])
            h2 = float(glob_data['hum2'])

        glob_data['temp_sr'] = round((t1 + t2) / 2, 1)
        glob_data['hum_sr'] = round((h1 + h2) /2, 1)
        app.set_data(glob_data)
            


        
        
        
        



