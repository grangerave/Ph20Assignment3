#Ph20 Assignment 3
#Numerical Solutions of ODE's
import numpy as np
import Grapher as g

def SetLabels(Xlab,Ylab,arg1,arg2,arg3):
    g.Xlabel = Xlab
    g.Ylabel = Ylab
    g.legend1 = arg1
    g.legend2 = arg2
    g.legend3 = arg3

def ExplicitSpringSim(X0,V0,K,m,h,N):
    #initialize array
    #format (t,x,v)
    output = np.zeros((N,3))
    #fill initial conditions
    output[0][1] = X0
    output[0][2] = V0
    for n in range(1,N):
        output[n][0] = n*h
        #X_i+1 = X_i + hV_i
        output[n][1]=output[n-1][1] + h*output[n-1][2]
        #V_i+1 = V_i - (K/m)hX_i
        output[n][2] = output[n-1][2] - h*(K/m)*output[n-1][1] 
    return output
    #g.ListPlot(output[:,0],output[:,1])

def ImplicitSpringSim(X0,V0,K,m,h,N):
    #initialize array
    #format (t,x,v)
    output = np.zeros((N,3))
    #fill initial conditions
    output[0][1] = X0
    output[0][2] = V0
    kk = K/m
    for n in range(1,N):
        output[n][0] = n*h
        #X_i+1 = X_i + hV_i
        output[n][1]=(output[n-1][1] + h*kk*output[n-1][2])*(1/(1+kk*h*h))
        #V_i+1 = V_i - (K/m)hX_i
        output[n][2] = (output[n-1][2] - h*kk*output[n-1][1])*(1/(1+kk*h*h)) 
    #g.ListPlot(output[:,0],output[:,1])
    return output

def SymplecticSpringSim(X0,V0,K,m,h,N):
    #initialize array
    #format (t,x,v)
    output = np.zeros((N,3))
    #fill initial conditions
    output[0][1] = X0
    output[0][2] = V0
    kk = K/m
    for n in range(1,N):
        output[n][0] = n*h
        #X_i+1 = X_i + hV_i
        output[n][1]=output[n-1][1] + h*output[n-1][2]
        #V_i+1 = V_i - (K/m)hX_i
        output[n][2] = -h*output[n-1][1]*kk + (1-h*h *kk)*output[n-1][2]
    #g.ListPlot(output[:,0],output[:,1])
    return output

n= 200
p= 40000
#X0,V0,K,m,h,N
output = ExplicitSpringSim(1,0,1,1,0.1,200)
output1 = ExplicitSpringSim(1,0,1,1,0.1,400)
output2 = ImplicitSpringSim(1,0,1,1,0.1,200)
output2a = ImplicitSpringSim(1,0,1,1,0.1,400)
output3 = SymplecticSpringSim(1,0,1,1,0.1,n)
output3a = SymplecticSpringSim(1,0,1,1,0.1,p)
outputP = SymplecticSpringSim(output3[n-1][1],output3[n-1][2],1,1,0.1,200)
outputQ = SymplecticSpringSim(output3a[p-1][1],output3a[p-1][2],1,1,0.1,200)

#Plot Explicit Position and Velocity (Oscillations1.png)
SetLabels('Time t','','Position','Velocity','')
g.ListPlot2(output[:,0],output[:,1],output[:,0],output[:,2],'Oscillations1')
#Plot Explicit Errors in pos and velocity (Errors.png)
SetLabels('Time t','','Position Error','Velocity Error','')
g.ListPlot2(output1[:,0],np.abs(output1[:,1] - np.cos(output1[:,0])),output1[:,0],np.abs(output1[:,2] + np.sin(output1[:,0])),'Errors')

def ErrorH():
    n = 8
    h0 = 0.1
    MaxErrors = np.zeros(n)
    h = np.zeros(n)
    for i in range(n):
        h[i] = h0/np.power(2,i)
        temp = ExplicitSpringSim(1,0,1,1,h0/np.power(2,i),400 * np.power(2,i))
        temp[:,1] = np.abs(temp[:,1] - np.cos(temp[:,0]))
        MaxErrors[i] = np.amax(temp[:,1])
    SetLabels('h','log(Max Error)','','','')
    g.ListLogPlot1(h,MaxErrors,'Error-H')


#truncation error (Error-H)
ErrorH()
#calculate power
E1 = np.power(output[:,1],2) + np.power(output[:,2],2)
E0 = np.power(output1[:,1],2) + np.power(output1[:,2],2)
E2 = np.power(output2[:,1],2) + np.power(output2[:,2],2)
E3 = np.power(output3[:,1],2) + np.power(output3[:,2],2)


#plot Explicit Power (Energy.png)
SetLabels('Time t','Normalized Total Energy','','','')
g.ListPlot(output[:,0],E1,'Energy')
#compare Energy to Error (ErrorCombination.png)
SetLabels('Time t','','Energy','Position Error','Velocity Error')
g.ListPlot3(output1[:,0],E0,output1[:,0],np.abs(output1[:,1] - np.cos(output1[:,0])),output1[:,0],np.abs(output1[:,2] + np.sin(output1[:,0])),'ErrorCombination')
#Implicit position and velocity (Implicit.png)
SetLabels('Time t','','Position','Velocity','')
g.ListPlot2(output2a[:,0],output2a[:,1],output2a[:,0],np.cos(output2a[:,0]),'Implicit')
#Implicit Error (ErrorIM.png)
SetLabels('Time t','','Explicit Error','Implicit Error','')
g.ListPlot2(output1[:,0],np.abs(output1[:,1] - np.cos(output1[:,0])),output2a[:,0],np.abs(output2a[:,1] - np.cos(output2a[:,0])),'ErrorIM')
#plot position v velocity for explicit and implicit (Spiral.png)
SetLabels('Position X','Velocity V','Explicit','Implicit','Symplectic')
g.ListPlot2(output[:,1],output[:,2],output2[:,1],output2[:,2],'Spiral')
#plot pos & velocity for explicit, implicit and symplectic (SpiralSymp.png)
g.ListPlot3(output[:,1],output[:,2],output2[:,1],output2[:,2],output3[:,1],output3[:,2],'SpiralSymp')
#Plot pos and velocity for symplectic (Symplectic.png)
SetLabels('Time t','','Position','Velocity','')
g.ListPlot2(output3[:,0],output3[:,1],output3[:,0],output3[:,2],'Symplectic')
#plot symplectic energy (EnergySym.png)
SetLabels('Time t','Normalized Total Energy','','','')
g.ListPlot(output3[:,0],E3,'EnergySym')
#plot energy comparison (Energy3.png)
SetLabels('Time t','Normalized Total Energy','Explicit','Implicit','Symplectic')
g.ListPlot3(output[:,0],E1,output2[:,0],E2,output3[:,0],E3,'Energy3')
#plot symplectic small time (SmallTime.png)
SetLabels('Time t','Normalized Total Energy','Explicit','Implicit','Symplectic')
g.ListPlot2(outputP[:,0] + n*0.1,outputP[:,1],outputP[:,0] + n*0.1,np.cos(outputP[:,0] + n*0.1),'SmallTime')
#plot symplectic large time (LargeTime.png)
SetLabels('Time t','Normalized Total Energy','Explicit','Implicit','Symplectic')
g.ListPlot2(outputQ[:,0] + p*0.1,outputQ[:,1],outputQ[:,0] + p*0.1,np.cos(outputQ[:,0] + p*0.1),'LargeTime')
#g.ListPlot3(output[:,0],E1,output2[:,0],E2,output3[:,0],E3)





