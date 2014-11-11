#reads input file in same directory, constructs a graph using pyplot
import numpy as np
import matplotlib.pyplot as plt

Xlabel = 'Time t'
Ylabel = 'Position X'
legend1 = 'Symplectic'
legend2 = 'Analytic'
legend3 = 'Symplectic'


def Labelize():
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.legend(loc = 2)

    
def ListPlot(x,y,fileName):
    plt.plot(x,y,color = 'r')
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.savefig(fileName + '.png')
    plt.close()
    
def ListPlot2(x1,y1,x2,y2,fileName):
    plt.plot(x1,y1,color = 'b',label = legend1)
    plt.plot(x2,y2,color = 'r',label = legend2)
    Labelize()
    #plt.show
    plt.savefig(fileName + '.png')
    plt.close()
    
def ListPlot3(x1,y1,x2,y2,x3,y3,fileName):
    plt.plot(x1,y1,color = 'b',label = legend1)
    plt.plot(x2,y2,color = 'r',label = legend2)
    plt.plot(x3,y3,color = 'g', label = legend3)
    Labelize()
    plt.savefig(fileName + '.png')
    plt.close()

def ListLogPlot(x1,y1):
    plt.loglog(x1,y1)
    Labelize()
    plt.show

def ListLogPlot1(x1,y1,fileName):
    plt.plot(x1,np.log(y1))
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.savefig(fileName + '.png')
    plt.close()