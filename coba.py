import snap7.client as c
from snap7.util import *
from snap7.snap7types import *

import sys
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
    # ser = serial.Serial('COM4', 9600)
    
    weight1 = ReadMemory(plc,88,0,S7WLReal)
    ratio1   = ReadMemory(plc,216,0,S7WLReal)
    sf1   = ReadMemory(plc,244,0,S7WLReal)
    af1   = ReadMemory(plc,120,0,S7WLReal)
    inv1 = ReadMemory(plc,402,0,S7WLReal)
    bs1 = ReadMemory(plc,692,0,S7WLReal)



    # print round(weight1,2)
    # print round(ratio1,2)
    # print round(sf1,2)
    # print round(af1,2)
    # print round(inv1,2)

    # print round(weight1,2),round(ratio1,2),round(sf1,2),round(af1,2),round(bs1,2),round(inv1,2),":"


    weight2 = ReadMemory(plc,92,0,S7WLReal)
    ratio2   = ReadMemory(plc,220,0,S7WLReal)
    sf2   = ReadMemory(plc,248,0,S7WLReal)
    af2   = ReadMemory(plc,124,0,S7WLReal)
    inv2 = ReadMemory(plc,406,0,S7WLReal)
    bs2 = ReadMemory(plc,696,0,S7WLReal)

    # print round(weight2,2)
    # print round(ratio2,2)
    # print round(sf2,2)
    # print round(af2,2)
    # print round(bs2,2)
    # print round(inv2,2)

    # print round(weight2,2),round(ratio2,2),round(sf2,2),round(af2,2),round(bs2,2),round(inv2,2),":"
    

    weight3 = ReadMemory(plc,96,0,S7WLReal)
    ratio3   = ReadMemory(plc,224,0,S7WLReal)
    sf3   = ReadMemory(plc,252,0,S7WLReal)
    af3   = ReadMemory(plc,128,0,S7WLReal)
    inv3 = ReadMemory(plc,410,0,S7WLReal)
    bs3 = ReadMemory(plc,700,0,S7WLReal)

    # print round(weight3,2)
    # print round(ratio3,2)
    # print round(sf3,2)
    # print round(af3,2)
    # print round(bs3,2)
    # print round(inv3,2)

    # print round(weight3,2),round(ratio3,2),round(sf3,2),round(af3,2),round(bs3,2),round(inv3,2),":"
    
    weight4 = ReadMemory(plc,100,0,S7WLReal)
    ratio4   = ReadMemory(plc,228,0,S7WLReal)
    sf4   = ReadMemory(plc,256,0,S7WLReal)
    af4   = ReadMemory(plc,132,0,S7WLReal)
    inv4 = ReadMemory(plc,414,0,S7WLReal)
    bs4 = ReadMemory(plc,704,0,S7WLReal)

    # print round(weight4,2)
    # print round(ratio4,2)
    # print round(sf4,2)
    # print round(af4,2)
    # print round(bs4,2)
    # print round(inv4,2)

    # print round(weight4,2),round(ratio4,2),round(sf4,2),round(af4,2),round(bs4,2),round(inv4,2),":"
    
    weight5 = ReadMemory(plc,104,0,S7WLReal)
    ratio5   = ReadMemory(plc,232,0,S7WLReal)
    sf5   = ReadMemory(plc,260,0,S7WLReal)
    af5   = ReadMemory(plc,136,0,S7WLReal)
    inv5 = ReadMemory(plc,418,0,S7WLReal)
    bs5 = ReadMemory(plc,708,0,S7WLReal)

    # print round(weight5,2)
    # print round(ratio5,2)
    # print round(sf5,2)
    # print round(af5,2)
    # print round(bs5,2)
    # print round(inv5,2)

    # print round(weight5,2),round(ratio5,2),round(sf5,2),round(af5,2),round(bs5,2),round(inv5,2),":"


    weight6 = ReadMemory(plc,108,0,S7WLReal)
    ratio6   = ReadMemory(plc,236,0,S7WLReal)
    sf6   = ReadMemory(plc,264,0,S7WLReal)
    af6   = ReadMemory(plc,140,0,S7WLReal)
    inv6 = ReadMemory(plc,422,0,S7WLReal)
    bs6 = ReadMemory(plc,712,0,S7WLReal)

    # print round(weight6,2)
    # print round(ratio6,2)
    # print round(sf6,2)
    # print round(af6,2)
    # print round(bs6,2)
    # print round(inv6,2)

    # print round(weight6,2),round(ratio6,2),round(sf6,2),round(af6,2),round(bs6,2),round(inv6,2),":"

    weight7 = ReadMemory(plc,112,0,S7WLReal)
    ratio7   = ReadMemory(plc,240,0,S7WLReal)
    sf7   = ReadMemory(plc,268,0,S7WLReal)
    af7   = ReadMemory(plc,144,0,S7WLReal)
    inv7 = ReadMemory(plc,426,0,S7WLReal)
    bs7 = ReadMemory(plc,716,0,S7WLReal)

    # print round(weight7,2)
    # print round(ratio7,2)
    # print round(sf7,2)
    # print round(af7,2)
    # print round(bs7,2)
    # print round(inv7,2)

    # print round(weight7,2),round(ratio7,2),round(sf7,2),round(af7,2),round(bs7,2),round(inv7,2)

    weight8 = ReadMemory(plc,116,0,S7WLReal)



    print round(weight1,2),round(ratio1,2),round(sf1,2),round(af1,2),round(bs1,2),round(inv1,1),":",round(weight2,2),round(ratio2,2),round(sf2,2),round(af2,2),round(bs2,2),round(inv2,1),":",round(weight3,2),round(ratio3,2),round(sf3,2),round(af3,2),round(bs3,2),round(inv3,1),":",round(weight4,2),round(ratio4,2),round(sf4,2),round(af4,2),round(bs4,2),round(inv4,1),":",round(weight5,2),round(ratio5,2),round(sf5,2),round(af5,2),round(bs5,2),round(inv5,1),":",round(weight6,2),round(ratio6,2),round(sf6,2),round(af6,2),round(bs6,2),round(inv6,1),":",round(weight7,2),round(ratio7,2),round(sf7,2),round(af7,2),round(bs7,2),round(inv7,1)



    # weight1 = ReadMemory(plc,88,0,S7WLReal)
    # weight2 = ReadMemory(plc,92,0,S7WLReal)
    # weight3 = ReadMemory(plc,96,0,S7WLReal)
    # weight4 = ReadMemory(plc,100,0,S7WLReal)
    # weight5 = ReadMemory(plc,104,0,S7WLReal)
    # weight6 = ReadMemory(plc,108,0,S7WLReal)
    # weight7 = ReadMemory(plc,112,0,S7WLReal)
    # weight8 = ReadMemory(plc,116,0,S7WLReal)

    # af1   = ReadMemory(plc,120,0,S7WLReal)
    # af2   = ReadMemory(plc,124,0,S7WLReal)
    # af3   = ReadMemory(plc,128,0,S7WLReal)
    # af4   = ReadMemory(plc,132,0,S7WLReal)
    # af5   = ReadMemory(plc,136,0,S7WLReal)
    # af6   = ReadMemory(plc,140,0,S7WLReal)
    # af7   = ReadMemory(plc,144,0,S7WLReal)
    # af8   = ReadMemory(plc,148,0,S7WLReal)

    # ratio1   = ReadMemory(plc,216,0,S7WLReal)
    # ratio2   = ReadMemory(plc,220,0,S7WLReal)
    # ratio3   = ReadMemory(plc,224,0,S7WLReal)
    # ratio4   = ReadMemory(plc,228,0,S7WLReal)
    # ratio5   = ReadMemory(plc,232,0,S7WLReal)
    # ratio6   = ReadMemory(plc,236,0,S7WLReal)
    # ratio7   = ReadMemory(plc,240,0,S7WLReal)

    # sf1   = ReadMemory(plc,244,0,S7WLReal)
    # sf2   = ReadMemory(plc,248,0,S7WLReal)
    # sf3   = ReadMemory(plc,252,0,S7WLReal)
    # sf4   = ReadMemory(plc,256,0,S7WLReal)
    # sf5   = ReadMemory(plc,260,0,S7WLReal)
    # sf6   = ReadMemory(plc,264,0,S7WLReal)
    # sf7   = ReadMemory(plc,268,0,S7WLReal)

    # inv1 = ReadMemory(plc,402,0,S7WLReal)
    # inv2 = ReadMemory(plc,406,0,S7WLReal)
    # inv3 = ReadMemory(plc,410,0,S7WLReal)
    # inv4 = ReadMemory(plc,414,0,S7WLReal)
    # inv5 = ReadMemory(plc,418,0,S7WLReal)
    # inv6 = ReadMemory(plc,422,0,S7WLReal)
    # inv7 = ReadMemory(plc,426,0,S7WLReal)

    # w1   = ReadMemory(plc,88,0,S7WLReal)
    # w2   = ReadMemory(plc,92,0,S7WLReal)
    # w3   = ReadMemory(plc,96,0,S7WLReal)
    # w4   = ReadMemory(plc,100,0,S7WLReal)
    # w5   = ReadMemory(plc,104,0,S7WLReal)
    # w6   = ReadMemory(plc,108,0,S7WLReal)
    # w7   = ReadMemory(plc,112,0,S7WLReal)
    # w8   = ReadMemory(plc,116,0,S7WLReal)





if __name__=="__main__":
    main()

    # print ReadMemory(plc,402,0,S7WLReal)
    # WriteMemory(plc,420,0,S7WLDWord,3.141592)
    # print ReadMemory(plc,420,0,S7WLDWord)

    #DONE!!

