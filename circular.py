from helpers import modFloor,calcEndpoint,LineBoundaries
from os import path

thickness=50
radius=170
buffer=5
increment=10

#important to remember you need actual values not just decimals



fileName=input('Enter file name')
if len(fileName)==0:fileName="testGcode"
fileName+='.txt'
f=None 


if path.isfile(fileName):f=open(fileName,"w")
else: f=open(fileName,"x")


f.write("G21\n")
#absolute mode
f.write("G90;\n")
4
#feed speed, possibly redundant
f.write("F25;\nF500;\n")

#assumes center start position 
f.write("G28.3 X0 Y0 Z0 ;\n")

x=0

yTarg=modFloor(radius-buffer,increment)
y=yTarg
#not sure if this is ideal
f.write(f"G1 X{x} Y{yTarg} Z0 ;(chilipeppr_pause);\n\n")

#can still do it otherwise, just only go as far as if it divisible
#deciding to work from center, even though it takes longer
#reason being is other wise, there could be some combinations of buffers and increments that wouldnt be centered a 0
yStart=yTarg
yFinish=-yTarg
downwards=True
rightwards=True
z=-60
zIncrement=30
zTarg=60

while(z<=zTarg):
    f.write(f"G1 X{x} Y{y} Z{z} ;\n\n")
    #need to consider endpoint, returning to that center spot
    while(y>=yFinish if downwards else y<=yFinish):
        y+=-increment if downwards else increment
        line=LineBoundaries(y)
        line.end=calcEndpoint(radius,y,increment,buffer)
        x=-line.end if rightwards else line.end
        xTarg=-x
        f.write(f"G1 X{x} Y{y}\n")
        #activating on edgecase
        print(rightwards)
        print(y,'xtarg',xTarg,'x',x)
        #error where the very end if off center
        while x<xTarg if rightwards else x>xTarg:
            x+=increment if rightwards else -increment
            f.write(f"G1 X{x} Y{y}\n")
        rightwards=False if rightwards else True
    downwards=False if downwards else True
    z+=zIncrement
    yFinish=-yFinish
    
f.write(f"G0 X0 Y0 Z{zTarg}")

#cable will stick out of fron
#f.write()



f.write(f"G0 X0 Y0 Z0")
f.close()
print('complete')
    