import matplotlib as mpl 
import matplotlib.pyplot as plt 
import math

print("Isoprocess programm")

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})



const=int(input("Print the constant. 1 if T, 2 if V and 3 if P: "))
value=float(input("Print the value of constant in SI: "))
graph=int(input("Print the function. 1 if PV, 2 if P/T, 3 if V/T: "))
if const==1:
    if graph==1:
        #PV=8.31T
        plt.axis([0, 250, 0, 250])
        plt.title('P(V)')
        plt.xlabel('V')
        plt.ylabel('P')

        Vs = []
        P_vals = []

        V = 0.1
        while V < 100000:
            P_vals += [ (8.31*value)/V ]
            Vs += [V]
            V += 0.1

        plt.plot(Vs, P_vals, color = 'blue', linestyle = 'solid',
                 label = 'P(v)')
        plt.show()
    if graph==2:
        plt.axis([0, 1000, 0, 100000])
        plt.title('P(T)')
        plt.xlabel('T')
        plt.ylabel('P')

        Ts = []
        P_vals = []

        x = 0.1
        while x < 100000:
            P_vals += [ x ]
            Ts += [value]
            x += 0.1
            

        plt.plot(Ts, P_vals, color = 'blue', linestyle = 'solid',
                 label = 'P(v)')
        plt.show()
    if graph==3:
        plt.axis([0, 1000, 0, 100000])
        plt.title('V(T)')
        plt.xlabel('T')
        plt.ylabel('V')

        Ts = []
        V_vals = []

        x = 0.1
        while x < 100000:
            V_vals += [ x ]
            Ts += [value]
            x += 0.1
            

        plt.plot(Ts, V_vals, color = 'blue', linestyle = 'solid',
                 label = 'P(v)')
        plt.show()
"""if const==2:
    
if const==3:"""
        
