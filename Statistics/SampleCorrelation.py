import math
from Statistics.Standarddeviation import Standarddeviation
from Statistics.Mean import Mean

class Samplecorrelation():
    @staticmethod
    def samplecorrelation(array):
        x = array[0]
        y = array[1]
        meanX = Mean.mean(x)
        meanY = Mean.mean(y)
        numerator = 0
        for index in range(len(x)):
            xdiff = x[index]-meanX
            ydiff = y[index]- meanY
            numerator += xdiff* ydiff
        covariance = numerator/ len(x)
        stdX = Standarddeviation.standarddeviation(x)
        stdY = Standarddeviation.standarddeviation(y)
        return covariance/(stdX*stdY)