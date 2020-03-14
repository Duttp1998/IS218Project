import unittest
from Calculator.StatisticsCalculator import StatsCalculator
from Random.Elements import Elements
from Random.Lists import Lists
from Random.Numbers import Numbers
from numpy.random import seed
from numpy.random import randint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        seed(5)
        self.testData = randint(10, 20, 30)
        self.statistics = StatsCalculator()
        self.seed = 1
        self.IntegerList = Lists.prandINTL(1, 100, 100, self.seed)
        self.FloatList = Lists.prandFLTL(1, 100, 100, self.seed)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, StatsCalculator)

    def test_mean_calculator(self):
        mean = self.statistics.Mean(self.testData)
        self.assertEqual(mean, 14)

    def test_median_calculator(self):
        median = self.statistics.Median(self.testData)
        self.assertEqual(median, 14.5)

    def test_mode_calculator(self):
        mode = self.statistics.Mode(self.testData)
        self.assertEqual(mode, 10)

    def test_variance_calculator(self):
        variance = self.statistics.Variance(self.testData)
        self.assertEqual(variance, 11)

    def test_skewness_calculator(self):
        skew = self.statistics.Skewness(self.testData)
        self.assertEqual(skew, 0.03576490724804414)

    def test_standarddeviation_calculator(self):
        standard = self.statistics.Standarddeviation(self.testData)
        self.assertEqual(standard, 3.3166247903554)

    def test_quartiles_calculator(self):
        quart = self.statistics.Quartiles(self.testData)
        self.assertEqual(quart, (11.0, 14.5, 17.0))

    def test_zscore_calculator(self):
        zscore = self.statistics.ZScore(self.testData)
        self.assertEqual(zscore, -1.276398025379199)

    def test_meandeviation_calculator(self):
        meand = self.statistics.MeanAbsoluteDeviation(self.testData)
        self.assertEqual(meand, 3.033333333333333)


    def test_populationcorrelation_calculator(self):
        popc = self.statistics.PopulationCorrelation(self.testData)
        self.assertEqual(popc, 3.3166247903554)
        print(results)

    def test_SimpleRandomSampling_calculator(self):
        results = self.statistics.SimpleRandomSampling(self.testData)
        self.assertEqual(results,  results )
        print(results)

    def test_ConfidenceIntervalPopulation_calculator(self):
        results = self.statistics.ConfidenceIntervalPopulation(0.9, self.testData)
        self.assertEqual(results,  results )
        print(results)

    def test_ConfidenceIntervalSample_calculator(self):
        results = self.statistics.ConfidenceIntervalSample(0.9, self.testData)
        self.assertEqual(results, results  )
        print(results)

    def test_MarginError_calculator(self):
        results = self.statistics.MarginError(self.testData)
        self.assertEqual(results, results  )
        print(results)

    def test_Cochran_calculator(self):
        results = self.statistics.Cochran(self.testData)
        self.assertEqual(results,  results )
        print(results)

    def test_SampleSizeUnknown_calculator(self):
        results = self.statistics.SampleSizeUnknown(self.testData, 0.9)
        self.assertEqual(results, results )
        print(results)
        
    def test_SampleSizeKnown_calculator(self):
        results = self.statistics.SampleSizeKnown(self.testData)
        self.assertEqual(results,  results)
        print(results)

if __name__ == '__main__':
    unittest.main()
