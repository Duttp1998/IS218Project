import PopulationSamplingfunctions
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.Quartiles import Quartiles
from Statistics.Skewness import Skewness
from Statistics.Standarddeviation import Standarddeviation
from Statistics.Variance import Variance

class StatsCalculator:
    Result = 0

    def __init__(self):
        pass

    def Mean(self, a):
        self.Result = Mean.mean(a)
        return self.Result

    def Median(self, a):
        self.Result = Median.median(a)
        return self.Result

    def Mode(self, a):
        self.Result = Mode.mode(a)
        return self.Result

    def Quartiles(self, a):
        self.Result = Quartiles.quartiles(a)
        return self.Result

    def Skewness(self, a):
        self.Result = Skewness.skewness(a)
        return self.Result

    def Standarddeviation(self, a):
        self.Result = Standarddeviation.standarddeviation(a)
        return self.Result

    def Variance(self, a):
        self.Result = Variance.variance(a)
        return self.Result



