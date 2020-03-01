#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:37:16 2020
#this scipts plots data from a txt file about river flows ,tqmean, and R-B index
@author: mcubbage
"""
#import numpy 
import numpy
numpy
# create function that create PDF od river flows, tqmean, and R-b index from a specific data file
def River_PDF (x, y):
    #import dataset
    tippe_data=numpy.genfromtxt(x, names=True) 
    #tippe_data=numpy.genfromtxt('/home/mcubbage/ABE65100/06-graphing-data-with-python-mcubbage12/Tippecanoe_River_at_Ora.Annual_Metrics.txt', names=True) 
    
    #import plotting 
    import matplotlib.pyplot as plt
    
    #plot mean, maximum, and minimum daily stream flows with different colors as first plot of a figure
    plt.subplot(311)
    plt.plot(tippe_data["Year"], tippe_data["Mean"], 'b', label='Mean')
    plt.plot(tippe_data["Year"], tippe_data["Max"], 'r', label='Max')
    plt.plot(tippe_data["Year"], tippe_data["Min"], 'b', label='Min')
    plt.xlabel("Year")
    plt.ylabel("Streamflow CFS")
    plt.legend()
    plt.show()
    
    
    #add a second plot to the figure of Tqmean
    plt.subplot(312)
    plt.plot(tippe_data["Year"],(tippe_data["Tqmean"]*100),'b^')
    plt.xlabel("Year")
    plt.ylabel("Tqmean (%)")
    plt.show()
    
    #add a third plot to the figure of RB index
    plt.subplot(313)
    plt.bar(tippe_data["Year"], tippe_data["RBindex"],)
    plt.xlabel("Year")
    plt.ylabel("R-B Index (ratio)")
    plt.show()

    #save figure as a PDF
    plt.savefig(y)
    
River_PDF ('/home/mcubbage/ABE65100/06-graphing-data-with-python-mcubbage12/Tippecanoe_River_at_Ora.Annual_Metrics.txt', 'Tippe_PDF.pdf')
River_PDF ('/home/mcubbage/ABE65100/06-graphing-data-with-python-mcubbage12/Wildcat_Creek_at_Lafayette.Annual_Metrics.txt', 'Wildcat_PDF.pdf')
