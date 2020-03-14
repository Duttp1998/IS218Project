import PopulationSamplingfunctions
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.Quartiles import Quartiles
from Statistics.Skewness import Skewness
from Statistics.Standarddeviation import Standarddeviation
from Statistics.Variance import Variance
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.SampleCorrelation import Samplecorrelation
from Statistics.Zscore import Zscore
from Statistics.Meandeviation import Meandeviation
from PopulationSamplingfunctions.Confidence_interval import ConfidenceInterval
from PopulationSamplingfunctions.Crochran import Cochran
from PopulationSamplingfunctions.Margin_error import MarginError
from PopulationSamplingfunctions.Random_sampling import RandomSample
from PopulationSamplingfunctions.Systematic_sampling import SystemicSample
from PopulationSamplingfunctions.Sample_size import SampleSize


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

    def Variance(self, a):
        self.Result = Variance.variance(a)
        return self.Result

    def Standarddeviation(self, a):
        self.Result = Standarddeviation.standarddeviation(a)
        return self.Result

    def Quartiles(self, a):
        self.Result = Quartiles.quartiles(a)
        return self.Result

    def Skewness(self, a):
        self.Result = Skewness.skewness(a)
        return self.Result

    def SampleCorrelation(self, a):
        self.Result = SampleCorrelation.samplecorrelation(a)
        return self.Result

    def PopulationCorrelation(self, a):
        self.Result = PopulationCorrelation.populationcorrelation(a)
        return self.Result

    def ZScore(self, a):
        self.Result = Zscore.zscore(a)
        return self.Result

    def MeanAbsoluteDeviation(self, a):
        self.Result = Meandeviation.meandeviation(a)
        return self.Result

    def SimpleRandomSampling(self, a, b, c):
        self.Result = RandomSample.random_sample(b, a, c)
        return self.Result

    def SimpleRandomSampling(self, a):
        self.Result = SystemicSample.systemicSample(a)
        return self.Result

    def ConfidenceIntervalPopulation(self, a, b):
        self.Result = ConfidenceInterval.confidenceIntervalPopulation(b, a)
        return self.Result

    def ConfidenceIntervalSample(self, a, b):
        self.Result = ConfidenceInterval.confidenceIntervalSample(b, a)
        return self.Result

    def MarginError(self, a):
        self.Result = MarginError.margin(a)
        return self.Result

    def Cochran(self, a):
        self.Result = Cochran.cochran(a)
        return self.Result

    def SampleSizeUnknown(self, a, b):
        self.Result = SampleSize.unknown_pop_sample(a, b)
        return self.Result

    def SampleSizeKnown(self, a):
        self.Result = SampleSize.known_pop_sample(a)
        return self.Result
