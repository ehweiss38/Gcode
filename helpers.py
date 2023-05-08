from math import sqrt,floor
        
class LineBoundaries:
    def __init__(self,y):
        self.y=y
        self.end=0
        self.r=0


def calcEndpoint(radius:float,y:float,increment:float,buffer:float):
    print()
    raw=sqrt(radius**2-y**2)
    val=floor(raw)
    #not radius-val actually 
    while (val%increment!=0 or raw-val<buffer) :
        #print(radius-val)
        val=val-1
        #print(val)
    return val

def modFloor(number,divisor):
    while number%divisor!=0:
        --number
    return number