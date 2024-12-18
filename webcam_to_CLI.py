import sys
import os
import cv2

import app_modes


#Starts the camera and forces it to give a frame (had some issues with it not working properly)
def webcamStart():
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if not vid.isOpened():
        vid.open(0)
        (ret,_) = vid.read()
        if not ret :
            while not ret :
                (ret,_) = vid.read()
    return vid

def main(argv,argc):
    #Base values
    mode="default"
    ramp = " .,;!vlLFE$"
    size = os.get_terminal_size()
    resX=size.columns
    resY=size.lines-1
    imagePath = ""
    setRes = False

    if((argc+1)%2 != 0) : 
        print("Bad arguments")
        return
    
    #Parameter selector
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
    
    #Mode selector
    match mode:
        case "ascii"|"a":
            vid = webcamStart()
            app_modes.ASCIIFlux(vid,ramp,resX,resY,setRes)
        case "greyscale" | "gr":
            vid = webcamStart()
            app_modes.greyScaleANSIFlux(vid,resX,resY,setRes)
        case "fullColor" | "fc" | "default" :
            vid = webcamStart()
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
