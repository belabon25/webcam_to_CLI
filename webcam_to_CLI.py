import sys
import os
import cv2

import app_modes

def main(argv,argc):
    mode="default"
    ramp = "@OEULi:. "
    dictChar = dict()
    size = os.get_terminal_size()
    resX=size.columns
    resY=size.lines-1
    imagePath = ""
    setRes = False
    for i in range(len(ramp)):
        dictChar[i]=ramp[-i]
    if((argc+1)%2 != 0) : 
        print("Mauvais arguments")
        return
    for i in range(1,argc,2):
        match argv[i]:
            case "-m"|"--mode":
                mode=argv[i+1]
            case "-x"|"--xRes":
                resX=int(argv[i+1])
                setRes = True
            case "-y"|"--yRes":
                resY=int(argv[i+1])   
                setRes = True 
            case "-i"|"--image-path":
                imagePath=argv[i+1]           
    
    match mode:
        case "ascii"|"a":
            vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            if not vid.isOpened():
                vid.open(0)
            (ret,_) = vid.read()
            if not ret :
                while not ret :
                    (ret,_) = vid.read()
            vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            app_modes.ASCIIFlux(vid,dictChar,resX,resY,setRes)
        case "greyscale" | "gr":
            vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            if not vid.isOpened():
                vid.open(0)
            (ret,_) = vid.read()
            if not ret :
                while not ret :
                    (ret,_) = vid.read()
            app_modes.greyScaleANSIFlux(vid,resX,resY,setRes)
        case "fullColor" | "fc" | "default" :
            vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            if not vid.isOpened():
                vid.open(0)
            (ret,_) = vid.read()
            if not ret :
                while not ret :
                    (ret,_) = vid.read()
            app_modes.fullColorANSIFlux(vid,resX,resY,setRes)
        case "loadimagefc" | "lifc" :
            if(imagePath==""): 
                print("Unset image path, please set the path using -i or --image-path.")
                return
            app_modes.printImageFC(imagePath,resX,resY)
        case "loadimagegr" | "ligr" :
            if(imagePath==""): 
                print("Unset image path, please set the path using -i or --image-path.")
                return  
            app_modes.printImageGR(imagePath,resX,resY)          
        case "debug":
            print("You found debug mode ! Nothing being tested at the moment...")


if __name__ == "__main__":
    main(sys.argv,len(sys.argv))
