import os
import cv2
import platform
import time

import w_cli_control

def ASCIIFlux(vid,dictChar,resX,resY,setRes) :
    dictlen = len(dictChar)
    if(platform.system() == "Windows"):
        os.system("cls")
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    else:
        os.system("clear")
    (_,frame) = vid.read()
    frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)  
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gr_n = gr
    gr_n = cv2.normalize(gr,gr_n,0,dictlen-1,cv2.NORM_MINMAX)
    w_cli_control.first_writeImageASCII(gr_n,dictChar)
    try:
        while(True):
            previousFrame=gr_n
            (_,frame) = vid.read()
            frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)  
            gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gr_n = gr
            gr_n = cv2.normalize(gr,gr_n,0,dictlen-1,cv2.NORM_MINMAX)
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
        if(platform.system() == "Windows"):
            os.system("cls")
        else:
            os.system("clear")
        print("Fin du programme.")

def greyScaleANSIFlux(vid,resX,resY,setRes):
    if(platform.system() == "Windows"):
        os.system("cls")
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    else:
        os.system("clear")
    (_,frame) = vid.read()
    frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)  
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gr_n = gr
    gr_n = cv2.normalize(gr,gr_n,0,23,cv2.NORM_MINMAX)
    w_cli_control.first_writeImageGR(gr_n)
    try:
        while(True):
            previousFrame=gr_n
            (_,frame) = vid.read()
            frame = cv2.resize(frame,(resX,resY),interpolation = cv2.INTER_AREA)  
            gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gr_n = gr
            gr_n = cv2.normalize(gr,gr_n,0,23,cv2.NORM_MINMAX)
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
        print("\033[0;37m\033[48;5;0m")
        if(platform.system() == "Windows"):
            os.system("cls")
        else:
            os.system("clear")
        print("Program terminated")

def fullColorANSIFlux(vid,resX,resY,setRes):
    if(platform.system() == "Windows"):
        os.system("cls")
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    else:
        os.system("clear")
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
        print("\033[0;37m\033[48;5;0m")
        if(platform.system() == "Windows"):
            os.system("cls")
        else:
            os.system("clear")
        print("Program terminated")    

def printImageGR(imagePath,resX,resY):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(resX,resY),interpolation = cv2.INTER_AREA)
    gr_n = img
    gr_n = cv2.normalize(img,gr_n,0,23,cv2.NORM_MINMAX)
    w_cli_control.first_writeImageGR(gr_n)
    print("\033[0;37m\033[48;5;0m")

def printImageFC(imagePath,resX,resY):
    img = cv2.imread(imagePath)
    img = cv2.resize(img,(resX,resY),interpolation = cv2.INTER_AREA)
    w_cli_control.first_writeImageFC(img)
    print("\033[0;37m\033[48;5;0m")