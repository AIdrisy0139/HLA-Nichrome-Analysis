import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Line 200 of csv 70985,5,1.21
#Capital T "T" refers to temperature
#Lowers t "t" refers to time
#Capital I "I" refers to current
file = open('Data5_4.csv', "r")

df = pd.read_csv(file, dtype={"TIME":float, "TEMP": float, "CURRENT" : float})
Volts = 5.0
data = df.values

ohms = (Volts/data.T[2])
ohms = np.expand_dims(ohms, axis=1)
data = np.append(data,ohms,axis=1)

data.T[0] = data.T[0]-257 #Makes the time start at 0

def graphTemps(data):
    plt.subplot(2,2,1)
    plt.plot(data.T[3],data.T[1]) #Temp vs Ohms
    plt.xlabel("Resistance")
    plt.ylabel("Temperature (Kelvin) ")
    plt.title("Temperature vs Resistance")

    plt.subplot(2,2,2)
    plt.plot(data.T[1],data.T[3])
    plt.title("Reistance vs Temperature")
    plt.xlabel("Temperature (Celcius)")
    plt.ylabel("Resistance (Ohms)")
    
    plt.subplot(2,2,3)
    plt.plot(data.T[2],data.T[1])
    plt.title("Temperature vs Current")
    plt.xlabel("Current")
    plt.ylabel("Temperature")

    plt.subplot(2,2,4)
    plt.plot(data.T[0],data.T[1])
    plt.title("Temperature vs Time")
    plt.xlabel("Time (ms)")
    plt.ylabel("Temperature (Celcius) ")

    plt.show()

def graphRITvt(data):
    plt.plot(data.T[0],data.T[3]) #Resistance 
    plt.plot(data.T[0],data.T[2]) #Current
    plt.plot(data.T[0],data.T[1])# Temperature
    plt.title("Resistance and Current vs Time")
    plt.xlabel("Time (ms) ")
    plt.ylabel("Resistance,Current,Temperature")
    plt.legend(["Resistance" ,"Current","Temperature"])
    plt.show()


def graphAll(data):
    graphTemps(data)
    graphRITvt(data)
graphAll(data)