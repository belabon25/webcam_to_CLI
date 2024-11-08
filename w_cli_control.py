def first_writeImageASCII(image,dictChar):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            s+= "\033[%d;%d;H" % (i+1, j+1) + dictChar[image[i][j]]
   print(s)    
def writeImageASCII(image,previousFrame,dictChar):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if((image[i][j] != previousFrame[i][j])):
               s+= "\033[%d;%d;H" % (i+1, j+1) + dictChar[image[i][j]]
   print(s)



def first_writeImageGR(image):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            s+= "\033[%d;%d;H" % (i+1, j+1) + "\033[48;5;%dm" % (232+image[i][j]) + " "
   print(s)
def writeImageGR(image,previousFrame):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if(image[i][j] != previousFrame[i][j]):
               s+= "\033[%d;%d;H" % (i+1, j+1) + "\033[48;5;%dm" % (232+image[i][j]) + " "
   print(s)



def first_writeImageFC(image):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            b, g, r = image[i][j];
            s+= "\033[%d;%d;H" % (i+1, j+1) + "\033[48;2;%d;%d;%dm" % (r,g,b) + " "
   print(s)    
def writeImageFC(image,previousFrame):
   s=""
   for i in range(len(image)) :
        for j in range(len(image[0])) :
            if((image[i][j] != previousFrame[i][j]).any()):
               b, g, r = image[i][j];
               s+= "\033[%d;%d;H" % (i+1, j+1) + "\033[48;2;%d;%d;%dm" % (r,g,b) + " "
   print(s)
