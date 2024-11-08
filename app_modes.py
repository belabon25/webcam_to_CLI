import os
import cv2
import platform
import time

import w_cli_control

def windowSetup():
    if(platform.system() == "Windows"):
        os.system("cls")
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    else:
        os.system("clear")

def readAndResize(vid,resX,resY):
    (_,frame) = vid.read()
    return cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)  

def convertAndNormalize(frame,ramp:255):
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gr_n = gr
    gr_n = cv2.normalize(gr,gr_n,0,ramp-1,cv2.NORM_MINMAX)
    return gr_n

def programExit():
    print('\033[0m')
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
    print("Program terminated")

def ASCIIFlux(vid,dictChar,resX,resY,setRes) :
    ramp = len(dictChar)
    windowSetup()
    frame = readAndResize(vid,resX,resY)
    gr_n = convertAndNormalize(frame,ramp)
    w_cli_control.first_writeImageASCII(gr_n,dictChar)
    try:
        while(True):
            previousFrame=gr_n
            frame = readAndResize(vid,resX,resY)
            gr_n = convertAndNormalize(frame,ramp)
            w_cli_control.writeImageASCII(gr_n,previousFrame,dictChar)
            if(not setRes) :
                size = os.get_terminal_size()
                if(resX != size.columns | resY != size.lines-1) :               
                    resX = size.columns
                    resY = size.lines-1
                    gr_n = cv2.resize(gr_n,(resX,resY),interpolation = cv2.INTER_AREA)
                    w_cli_control.first_writeImageASCII(gr_n,dictChar)
            time.sleep(1/30)
    except KeyboardInterrupt:
        programExit()

def greyScaleANSIFlux(vid,resX,resY,setRes):
    windowSetup()
    frame = readAndResize(vid,resX,resY)
    gr_n = convertAndNormalize(frame,23)
    w_cli_control.first_writeImageGR(gr_n)
    try:
        while(True):
            previousFrame=gr_n
            frame = readAndResize(vid,resX,resY)
            gr_n = convertAndNormalize(frame,23)
            w_cli_control.writeImageGR(gr_n,previousFrame)
            if(not setRes) :
                size = os.get_terminal_size()
                if(resX != size.columns | resY != size.lines-1) :               
                    resX = size.columns
                    resY = size.lines-1
                    gr_n = cv2.resize(gr_n,(resX,resY),interpolation = cv2.INTER_AREA)
                    w_cli_control.first_writeImageGR(gr_n)
            time.sleep(1/30)
    except KeyboardInterrupt:
        programExit()

def fullColorANSIFlux(vid,resX,resY,setRes):
    windowSetup()
    (_,frame) = vid.read()
    frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)
    w_cli_control.first_writeImageFC(frame)
    try:
        while(True):
            previousFrame=frame
            (_,frame) = vid.read()
            frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)
            w_cli_control.writeImageFC(frame,previousFrame)
            if(not setRes) :
                size = os.get_terminal_size()
                if(resX != size.columns | resY != size.lines-1) :               
                    resX = size.columns
                    resY = size.lines-1
                    frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)
                    w_cli_control.first_writeImageFC(frame)
            time.sleep(1/30)
    except KeyboardInterrupt:
        programExit()

def printImageGR(imagePath,resX,resY):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(resX,resY),interpolation = cv2.INTER_AREA)
    gr_n = img
    gr_n = cv2.normalize(img,gr_n,0,23,cv2.NORM_MINMAX)
    w_cli_control.first_writeImageGR(gr_n)

def printImageFC(imagePath,resX,resY):
    img = cv2.imread(imagePath)
    img = cv2.resize(img,(resX,resY),interpolation = cv2.INTER_AREA)
    w_cli_control.first_writeImageFC(img)