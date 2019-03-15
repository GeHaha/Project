# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:53:37 2019

@author: Gehaha
"""

import crcmod

def CalCRC16(data ,length):
    print(data ,length)
    crc = 0xFFFF
    if length == 0:
        length = 1

    #for j in data
    ## crc ^= j
    j = 0
    while length != 0:
        crc ^= list.__getitem__(data,j)
       # print('j = 0x%02x,length = 0x%02x,crc =0x%04x' %(j,length,crc))
        for i in range(0,8):
            if crc & 1:
                crc >>=1
                crc ^= 0xA001
            else:
                crc >>= 1
        length -= 1
        j += 1
        ## if length == 0
        ## break
    return crc

def CheckCRC(data,length,crctype):
    if length < 3:
        print('The data len(%d) is less than3 3!!!',length)
        return 0
    crc_res = 0
    tmp = [0,0,0,0]
    if crctype == 0:
        crc_res = CalCRC16(data,length-2)
        tmp[0] = crc_res & 0xFF
        tmp[1] = (crc_res >> 8) & 0xFF

        if data[length-2] == tmp[0] and data[length-1] == tmp[1]:
            return 1
    elif crctype == 1:
        print('CRC32 is not support...')
        return 0
    
#测试专用
if __name__ == '__mian__':
    crc16 = crcmod.mkCrcFun(0x18005,initCrc = 0xFFFF ,rev = True,xorOut = 0x0000)
    crc_array = b'0xFE 0XFD'
    crc_calc = crc16(crc_array) #j计算得到的crc
    a= hex(crc_calc)
    print(crc_calc,a )

    crc_value = [0x01, 0x04, 0x13, 0x87, 0x00, 0x30]
    crc_transformation = CalCRC16(crc_value, len(crc_value))
    crc_calculation = hex(crc_transformation)
    # print('crc_calculation:',crc_calculation)
    tasd = [0x00, 0x00]
    tasd[0] = crc_transformation & 0xFF
    tasd[1] = (crc_transformation >> 8) & 0xFF
    H = hex(tasd[0])
    L = hex(tasd[1])
    H_value = int(H, 16)
    L_value = int(L, 16)
    crc_value.append(H_value)
    crc_value.append(L_value)
    print(crc_value)  # calculation value   CRC

    # ========================================================
    print('\n')
    # crc_value2 = [0x01, 0x04, 0x13, 0x87, 0x00, 0x30,0x44,0xB3]
    # print('crc_value2:',crc_value2)
    # crc_cheak=CheckCRC(crc_value2,len(crc_value2),0)

    crc_check = CheckCRC(crc_value, len(crc_value), 0)
    if crc_check == 1:
        print('Right')
    else:
        print('wrong')

    print(crc_check)  # check calculation value
