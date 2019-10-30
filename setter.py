import snap7.client as c
from snap7.util import *
from snap7.snap7types import *

import sys
import time
from os import system, name

plc = c.Client()
plc.connect('192.168.0.180',0,1)

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

def fmotor(no,hz):
    if no == "1":
        WriteMemory(plc,402,0,S7WLReal,float(hz))

    elif no == "2":
        WriteMemory(plc,406,0,S7WLReal,float(hz))

    elif no == "3":
        WriteMemory(plc,410,0,S7WLReal,float(hz))

    elif no == "4":
        WriteMemory(plc,414,0,S7WLReal,float(hz))

    elif no == "5":
        WriteMemory(plc,418,0,S7WLReal,float(hz))

    elif no == "6":
        WriteMemory(plc,422,0,S7WLReal,float(hz))

    elif no == "7":
        WriteMemory(plc,426,0,S7WLReal,float(hz))


def frate(r):
    WriteMemory(plc,334,0,S7WLReal,float(r))

def fratio(hopper,rat):
    if hopper == "1":
        WriteMemory(plc,216,0,S7WLReal,float(rat))

    elif hopper == "2":
        WriteMemory(plc,220,0,S7WLReal,float(rat))

    elif hopper == "3":
        WriteMemory(plc,224,0,S7WLReal,float(rat))

    elif hopper == "4":
        WriteMemory(plc,228,0,S7WLReal,float(rat))

    elif hopper == "5":
        WriteMemory(plc,232,0,S7WLReal,float(rat))

    elif hopper == "6":
        WriteMemory(plc,236,0,S7WLReal,float(rat))

    elif hopper == "7":
        WriteMemory(plc,240,0,S7WLReal,float(rat))

def wlength(hopper,length):
    if hopper == "1":
        WriteMemory(plc,724,0,S7WLReal,float(length))

    elif hopper == "2":
        WriteMemory(plc,728,0,S7WLReal,float(length))

    elif hopper == "3":
        WriteMemory(plc,732,0,S7WLReal,float(length))

    elif hopper == "4":
        WriteMemory(plc,736,0,S7WLReal,float(length))

    elif hopper == "5":
        WriteMemory(plc,740,0,S7WLReal,float(length))

    elif hopper == "6":
        WriteMemory(plc,744,0,S7WLReal,float(length))

    elif hopper == "7":
        WriteMemory(plc,748,0,S7WLReal,float(length))
    
    elif hopper == "8":
        WriteMemory(plc,752,0,S7WLReal,float(length))

def selesai():
    system('cls')
    print "perintah telah sukses dilaksanakan"
    time.sleep(1)

def awal():
    # rate 10
    # ratio 1 20
    # length 1 1.2365

    command = sys.argv[1]
    # number = sys.argv[2]
    # value = sys.argv[3]

    if command == "rate" :
        # rate = raw_input("--berapa rate yang anda inginkan ? : ")
        number = sys.argv[2]

        frate(number)
        # selesai()

    elif command == "ratio" :
        number = sys.argv[2]   
        value = sys.argv[3]

        hopper = number # raw_input("--hopper no berapa yang anda ingin rubah ? : ")
        ratio = value # raw_input("----masukkan nilai persentase ratio yang baru : ")
        fratio(hopper,ratio)
        # selesai()

    elif name == "length" :
        number = sys.argv[2]
        value = sys.argv[3]
        
        belt = number #raw_input("--hopper / belt no berapa yang anda ingin rubah ? : ")
        value = value #raw_input("----masukkan nilai weighing length yang baru : ")
        wlength(belt,value)
        # selesai()

    # elif name == "3" :
    #     motor = raw_input("--motor no berapa yang anda ingin rubah frekuensinya? : ")
    #     freq = raw_input("----masukkan nilai frekuensi motor yang baru : ")
    #     fmotor(motor,freq)
    #     selesai()

    else:
        print "input anda salah.."
        # time.sleep(1)


if __name__=="__main__":
    awal()
    # main()

    # print ReadMemory(plc,402,0,S7WLReal)
    # WriteMemory(plc,420,0,S7WLDWord,3.141592)
    # print ReadMemory(plc,420,0,S7WLDWord)

    #DONE!!

