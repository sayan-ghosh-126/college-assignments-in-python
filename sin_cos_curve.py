import matplotlib.pyplot as plt
import math
def SinCurve():
    plt.subplot(2,1,1)
    degree=range(0,360+1)
    SinValue=[math.sin(math.radians(i)) for i in degree]
    plt.plot(SinValue)
    plt.xlabel("degree")
    plt.ylabel("SinValue")
    plt.title("SinCurve")
    plt.grid()
def CosCurve():
    plt.subplot(2,1,2)
    degree=range(0,360+1)
    CosValue=[math.sin(math.radians(i)) for i in degree]
    plt.plot(CosValue)
    plt.xlabel("degree")
    plt.ylabel("CosValue")
    plt.title("CosCurve")
    plt.grid() 
SinCurve()
CosCurve()
plt.tight_layout()
plt.show()       