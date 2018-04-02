import serial


arduino = serial.Serial('/dev/ttyACM2', 9600)


while True:
    try:
        result = {}
        res_text = ""
        data = arduino.readline()
        data = data[:-2]
        data = data.decode('utf-8')
        data_list = data.split(",")
        if len(data_list) > 6:
            result['pipe'] = data_list[0]
            result['temp1'] = data_list[1]
            result['hum1'] = data_list[2]
            result['modeBMP'] = data_list[3]
            result['temp2'] = data_list[4]
            result['hum2'] = data_list[5]
            result['press'] = data_list[6]
            for key in result:
                res_text += "{0}: {1} ".format(key, str(result[key])).ljust(18, ' ')
        print(res_text)
    except:
        break


arduino.close()
