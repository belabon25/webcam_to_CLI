
#ASCII image writing
# \033[%d;%d;H is the ANSI escape sequence for cursor handling, i being the column and j being the line (if i remember correctly)
def first_writeImageASCII(image,ramp):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            s+= "\033[%d;%d;H" % (i+1, j+1) + ramp[image[i][j]]
   print(s)    
def writeImageASCII(image,previousFrame,ramp):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if((image[i][j] != previousFrame[i][j])):
               s+= "\033[%d;%d;H" % (i+1, j+1) + ramp[image[i][j]]
   print(s)


#Greyscale image writing
# \033[%d;%d;H is the ANSI escape sequence for cursor handling, i being the column and j being the line (if i remember correctly)
# \033[48;5;%dm represent the background color of the character (which is the ' ' written just after the m)
# Here, we use the 255 color mode, 232 from 255 are different shades of grey (refer to https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
def first_writeImageGR(image):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            s+= "\033[%d;%d;H\033[48;5;%dm " % (i+1, j+1,232+image[i][j])
   print(s)
def writeImageGR(image,previousFrame):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if(image[i][j] != previousFrame[i][j]):
               s+= "\033[%d;%d;H\033[48;5;%dm " % (i+1, j+1,232+image[i][j])
   print(s)


#Full color image writing
# \033[%d;%d;H is the ANSI escape sequence for cursor handling, i being the column and j being the line (if i remember correctly)
# \033[48;2;%d;%d;%dm represent the background color of the character (which is the ' ' written just after the m)
#Here, we use the full scale of color available by combinaison of RGB value, each primary color scaling from 0 to 255
def first_writeImageFC(image):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            b, g, r = image[i][j];
            s += "\033[%d;%d;H\033[48;2;%d;%d;%dm " % (i+1, j+1, r,g,b)
   print(s)    
def writeImageFC(image,previousFrame):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if((image[i][j] != previousFrame[i][j]).any()):
               b, g, r = image[i][j]
               s+= "\033[%d;%d;H\033[48;2;%d;%d;%dm " % (i+1, j+1, r,g,b)
   print(s)
