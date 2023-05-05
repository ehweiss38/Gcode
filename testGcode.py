from os import path

fileName="testG.txt"
f=None 
if path.isfile(fileName):f=open(fileName,"w")
else: f=open(fileName,"x")

#Type dimensions here (#mm):

inch=25.4
#total length of x axis
xSpan=500
ySpan=500
zMax=6*inch

#distance to move between measurements
xIncrement=10 
yIncrement=10
zIncrement=2*inch

#metric units
f.write("G21\n")
#absolute mode
f.write("G90;\n")

#feed speed, possibly redundant
f.write("F25;\nF500;\n")

#assumes center start position 
f.write("G28.3 X0 Y0 Z0 ;\n")
	


f.write(f"G0 X-{xSpan/2} Y{ySpan/2} Z0 ;(chilipeppr_pause);\n\n")

downwards=True
z=0
while(z<=zMax):
    lowY=ySpan/2 if downwards else -1*ySpan/2
    highY=-1*lowY
    rightwards=True
    y=lowY
    while((downwards and y>=highY) or (downwards==False and y<=highY)):
        lowX=-1*xSpan/2 if rightwards else xSpan/2
        highX=-1*lowX
        x=lowX
        while (x!=highX):
            x+=xIncrement if rightwards else -1*xIncrement
            f.write(f"G1 X{x} (chilipeppr pause);\n")
            f.write("G4 P1\n")
    
        if y!=highY:y+=-1*yIncrement if downwards else yIncrement
        else: break
        f.write(f"G0 X{highX} Y{y} Z{z} (chilipeppr_pause);G4 P1;\n")
        rightwards=False if rightwards else True
        print(f"{y}-y {z}-z level complete\n")
    if z!=zMax:z+=zIncrement
    else:break
    f.write(f"G0 X{highX} Y{highY} Z{z} (chilipeppr_pause);G4 P1;\n")
    downwards=False if downwards else True
    print(f"{z} z level complete\n")

f.write(f"G0 X0 Y0;")
f.write(f"G X0 Y0 Z0;")
print('closing')
f.close()