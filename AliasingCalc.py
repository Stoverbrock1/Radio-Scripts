import numpy as np
import matplotlib.pyplot as plt


"""
aliasingFreq() returns the aliased frequency given the sampling
rate and the input frequency. There is also funcitonality for
plotting said frequencies, i.e.
aliasingFreq(Sampling Frequency, Input Frequency, Plot(= True or False)):
    ...
    return Aliased Frequency


insert "from AliasingCalc import aliasingFreq" to use function

"""



def aliasingFreq(samplingF, inputF, plot=True):
    NyF = samplingF/2
    aliased = inputF
    done = False
    while (done == False):
        if ((aliased <= NyF) and (aliased >= 0)):
            done = True
        elif (aliased < 0):
            aliased = abs(aliased)
        else:
            aliased = NyF - (aliased - NyF)
    if (plot==True):
        plt.axvline(samplingF, color='blue', label='Sampling Frequency = '+ str(samplingF))
        plt.axvline(NyF, linewidth=5, color='grey', label='Nyquist Frequency = ' + str(NyF))
        plt.axvline(aliased, color='green', label='Aliased Frequency = ' + str(aliased))
        plt.axvline(inputF, color='red', label='Input Frequency = ' + str(inputF))
        plt.xlim(0)
        plt.xlabel("Frequency")
        plt.legend()
    return aliased
