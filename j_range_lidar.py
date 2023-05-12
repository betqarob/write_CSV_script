import serial, time
from script_csv import * 

SIZE = 7 # change number depending on the amount of lidars
BAUD_RATE = 115200
DEV = "/dev/ttyUSB"

my_serial = []

for x in range(SIZE):
    my_serial.append(serial.Serial(DEV + str(x), BAUD_RATE))

class RangeRead:
    '''
    set to mm for measurement unit
    command 5A 05 05 06 6A - set to mm
    command 5A 05 05 01 65 - set to cm
    command 5A 04 11 6F - save settings
    ser.write ('5A 05 05 01 65')
    '''
    def __init__(self):
        self.init()

    #configures all the lidars to be set to mm measurement
    def init(self):
        for x in range(len(my_serial)):
            my_serial[x].write('5A 05 05 01 65')
            my_serial[x].write('5A 04 11 6F')
            my_serial[x].reset_input_buffer()
    
    # modified the function to read from all devices and store it into a csv script.
    def getTFminiData(self):
        while True:
            for x in range(SIZE):
                count = my_serial[x].in_waiting
                if count > 9:
                    recv = my_serial[x].read(9)
                    my_serial[x].reset_input_buffer()
                    if (recv[0] == 'Y' and recv[1] == 'Y'):
                        low = int(recv[2].encode('hex'), 16)
                        high = int(recv[3].encode('hex'), 16)
                        distance = low + (high << 8)
                        
                        script.data_append(distance, x)
                        #print(distance, 'mm')
                        # change the sleep time to change how many data points you are collecting [if you want it to be live or record every 3 seconds]
                        time.sleep(.5)
            script.append_csv('testing1.csv')

# modified the main to close all devices and create the csv file.
if __name__ == '__main__':
    try:
        script = script_csv('testing1.csv')
        if my_serial[0].is_open == False:
            my_serial[0].open()
        reader = RangeRead()
        reader.getTFminiData()
    except KeyboardInterrupt: #Ctrl+C
        if my_serial[0] != None:
            my_serial[0].close()
        script.remove_blanks('testing1.csv', 'testing_clean1.csv')
