import matplotlib.pyplot as plt
def PlotHistogram(data):
    plt.hist(data)
    plt.xlabel("value")
    plt.ylabel("frequency")
    plt.title("Histogram")
    plt.xlim(min(data)-1,max(data)-1)
    plt.show()
data=(input("enter data to be ploted histogram:"))
PlotHistogram(data)    
