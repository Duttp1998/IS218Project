import unittest
from numpy.random import seed
from numpy.random import randint

from Statistics.Skewness import Skewness
from Statistics.Median import Median
from Statistics.Variance import Variance
from Statistics.Standarddeviation import Standarddeviation
from Statistics.Zscore import Zscore
from Statistics.Meandeviation import Meandeviation
from Statistics.Quartiles import Quartiles
from Statistics.SampleCorrelation import Samplecorrelation
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.Statistics import Statistics
from Statistics.Mode import Mode
from Statistics.Mean import Mean


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(10, 20, 30)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 54.47)

    def test_median_calculator(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 57.0 )

    def test_mode_calculator(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 98)

    def test_variance_calculator(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 884.1708080808081)

    def test_skewness_calculator(self):
        skew = Skewness.skewness(self.testData)
        self.assertEqual(skew, -0.21197867987065927)

    def test_standarddeviation_calculator(self):
        standard = Standarddeviation.standarddeviation(self.testData)
        self.assertEqual(standard, 29.735009804619338)

    def test_quartiles_calculator(self):
        quart = Quartiles.quartiles(self.testData)
        self.assertEqual(quart, (11.0, 14.5, 17.0))

    def test_zscore_calculator(self):
        zscore = Zscore.zscore(self.testData)
        self.assertEqual(zscore, -1.2326792344561226)

    def test_meandeviation_calculator(self):
        meand = Meandeviation.meandeviation(self.testData)
        self.assertEqual(meand, 25.09240000000001)

    def test_samplecorrelation_calculator(self):
        samplec = Samplecorrelation.samplecorrelation(self.testData)
        self.assertEqual(samplec, 3.3166247903554)

    def test_populationcorrelation_calculator(self):
        popc = PopulationCorrelation.populationcorrelation(self.testData)
        self.assertEqual(popc, 3.3166247903554)


if __name__ == '__main__':
    unittest.main()