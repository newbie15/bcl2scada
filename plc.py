import snap7.client as c
from snap7.util import *
from snap7.snap7types import *

import serial
import time
from os import system, name


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas["MK"],0,byte,result)

def main():
    plc = c.Client()
    plc.connect('192.168.0.180',0,1)
    ser = serial.Serial('COM4', 9600)

    while True:

        print "    ____  ________   ___                    _       __             "
        print "   / __ )/ ____/ /  |__ \    _      _____  (_)___ _/ /_  ___  _____"
        print "  / __  / /   / /   __/ /   | | /| / / _ \/ / __ `/ __ \/ _ \/ ___/"
        print " / /_/ / /___/ /___/ __/    | |/ |/ /  __/ / /_/ / / / /  __/ /    "
        print "/_____/\____/_____/____/    |__/|__/\___/_/\__, /_/ /_/\___/_/     "
        print "                                          /____/                   "



        inv1 = ReadMemory(plc,402,0,S7WLReal)
        inv2 = ReadMemory(plc,406,0,S7WLReal)
        inv3 = ReadMemory(plc,410,0,S7WLReal)
        inv4 = ReadMemory(plc,414,0,S7WLReal)
        inv5 = ReadMemory(plc,418,0,S7WLReal)
        inv6 = ReadMemory(plc,422,0,S7WLReal)
        inv7 = ReadMemory(plc,426,0,S7WLReal)

        print ""
        print "==================================================================="
        print ""
        print "  Inverter 1", round(inv1,1),"Hz"
        print "  Inverter 2", round(inv2,1),"Hz"
        print "  Inverter 3", round(inv3,1),"Hz"
        print "  Inverter 4", round(inv4,1),"Hz"
        print "  Inverter 5", round(inv5,1),"Hz"
        print "  Inverter 6", round(inv6,1),"Hz"
        print "  Inverter 7", round(inv7,1),"Hz"
        print ""
        print ""
        print ""
        print "  kirim perintah :"
        print ""

        # inv1 = 5
        # inv2 = 10
        # inv3 = 15
        # inv4 = 20
        # inv5 = 25
        # inv6 = 30
        # inv7 = 35

        v1 = round(inv1/10,2)
        v2 = round(inv2/10,2)
        v3 = round(inv3/10,2)
        v4 = round(inv4/10,2)
        v5 = round(inv5/10,2)
        v6 = round(inv6/10,2)
        v7 = round(inv7/10,2)

        print "    ",(v1,v2,v3,v4,v5,v6,v7)
        ser.write(str(v1))
        ser.write(";")
        ser.write(str(v2))
        ser.write(";")
        ser.write(str(v3))
        ser.write(";")
        ser.write(str(v4))
        ser.write(";")
        ser.write(str(v5))
        ser.write(";")
        ser.write(str(v6))
        ser.write(";")
        ser.write(str(v7))
        ser.writelines("")

        time.sleep(1)
        ser.flushInput()
        system('cls')


if __name__=="__main__":
    main()

    # print ReadMemory(plc,402,0,S7WLReal)
    # WriteMemory(plc,420,0,S7WLDWord,3.141592)
    # print ReadMemory(plc,420,0,S7WLDWord)

    #DONE!!

