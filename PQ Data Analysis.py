# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:07:36 2016

@author: Gautam
"""
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import math

#Desigin Filter
def build_filter(n,Vs,QF):
    w = 2*3.141*50
    Q = (8e-6)*(2*w*(Vs^2))
    L = 1/(n*n*w*w*8e-6)
    R = (n*w*L)/QF
    return Q,L,R

#Checking for Harmonic Resonance
def check_harmonic(C,L,n):
    if 50 == int(1/(2*3.141*n*math.sqrt(8e-6*L))):
        return True
    else:
        return False

def data_plot(data2system,data4system,data6system,data9system,ylabel,num):
    x    = np.arange(0.0,156.0,1)
    fig1 = plt.figure(num, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
    z    = (num*100)+11
    ax   = fig1.add_subplot(z)
    ax.set_xlabel('Time')
    ax.set_ylabel(ylabel)
    ax.set_title(str(ylabel)+' for different loads')
    plt.plot(x,data2system,'b-',label="2system")
    plt.plot(x,data4system,'g-',label="4system")
    plt.plot(x,data6system,'r-',label="6system")
    plt.plot(x,data9system,'y-',label="9system")
    plt.legend()
    return plt.show()

    
#Opeing Excel File to Read data        
book1 = xlrd.open_workbook("C:\Users\gautam\Desktop\PQ-Data-2system.xlsx")
book2 = xlrd.open_workbook("C:\Users\gautam\Desktop\PQ-Data-4system.xlsx")
book3 = xlrd.open_workbook("C:\Users\gautam\Desktop\PQ-Data-6system.xlsx")
book4 = xlrd.open_workbook("C:\Users\gautam\Desktop\PQ-Data-9system.xlsx")

first_sheet_1 = book1.sheet_by_index(0)
first_sheet_2 = book2.sheet_by_index(0)
first_sheet_3 = book3.sheet_by_index(0)
first_sheet_4 = book4.sheet_by_index(0)

#Collecting Data
IHD3_data1 = first_sheet_1.col_values(colx=3,start_rowx=1,end_rowx=157)
IHD3_data2 = first_sheet_2.col_values(colx=3,start_rowx=1,end_rowx=157)
IHD3_data3 = first_sheet_3.col_values(colx=3,start_rowx=1,end_rowx=157)
IHD3_data4 = first_sheet_4.col_values(colx=3,start_rowx=1,end_rowx=157)

IHD3_data1_avg = np.mean(IHD3_data1)
IHD3_data2_avg = np.mean(IHD3_data2)
IHD3_data3_avg = np.mean(IHD3_data3)
IHD3_data4_avg = np.mean(IHD3_data4)

IHD5_data1 = first_sheet_1.col_values(colx=4,start_rowx=1,end_rowx=157)
IHD5_data2 = first_sheet_2.col_values(colx=4,start_rowx=1,end_rowx=157)
IHD5_data3 = first_sheet_3.col_values(colx=4,start_rowx=1,end_rowx=157)
IHD5_data4 = first_sheet_4.col_values(colx=4,start_rowx=1,end_rowx=157)

IHD5_data1_avg = np.mean(IHD5_data1)
IHD5_data2_avg = np.mean(IHD5_data2)
IHD5_data3_avg = np.mean(IHD5_data3)
IHD5_data4_avg = np.mean(IHD5_data4)



#Plotting
data_plot(IHD3_data1,IHD3_data2,IHD3_data3,IHD3_data4,'IHD3',1)
data_plot(IHD5_data1,IHD5_data2,IHD5_data3,IHD5_data4,'IHD5',2)

#Filter Design
reactive_power = first_sheet_1.col_values(colx=9,start_rowx=1,end_rowx=157)
Reactive_power = (reactive_power)
avg_reactive_power = np.mean(Reactive_power)
max_reactive_power = max(reactive_power)
filter_values_3 = build_filter(3,221,50)
filter_values_5 = build_filter(5,221,50)
harmonic_resonance_3 = check_harmonic(filter_values_3[0],filter_values_3[1],3)
harmonic_resonance_5 = check_harmonic(filter_values_5[0],filter_values_5[1],5)

#Logging
log = open("C:\Users\gautam\Desktop\PQ Datalog.txt","a")
log.write("Avg Reactive Power: "+str(avg_reactive_power))
log.write("\nFilter values for 3rd harmonic component: "  +str(filter_values_3))
log.write("\nFilter values for 5th harmonic component: "  +str(filter_values_5))
log.write("\nHarmonic Resonance for 3rd harmonic filter: "+str(harmonic_resonance_3))
log.write("\nHarmonic Resonance for 5th harmonic filter: "+str(harmonic_resonance_5))
log.write("\n----------------------------------------------------------------------------------------------\n")
log.close()



